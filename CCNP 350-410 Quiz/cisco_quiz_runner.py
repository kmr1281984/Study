#!/usr/bin/env python3
"""
cisco_quiz_runner.py — CSV-driven quiz app with domain selection (CCNP-friendly)

CSV required columns:
  id, domain, type, question, A, B, C, D, answer
Optional:
  explanation, tags

Features:
- Filter by domain(s): --domains "Infrastructure,Security"
- List domains: --list-domains
- Shuffle questions: --shuffle
- Limit number of questions: --limit 25
- Timed mode per question: --time-per-q 45
- Weighted sampling by domain (useful when mixing domains): --weighted
- Review missed questions at end: --review-missed
- Save results to JSONL: --save results.jsonl

Usage examples:
  python cisco_quiz_runner.py --csv ccnp_350_401.csv --list-domains
  python cisco_quiz_runner.py --csv ccnp_350_401.csv --domains "Infrastructure,Security" --shuffle --limit 20
  python cisco_quiz_runner.py --csv ccnp_350_401.csv --domains "Automation" --time-per-q 60 --review-missed
"""

from __future__ import annotations
import argparse
import csv
import json
import random
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple


CHOICES = ("A", "B", "C", "D")


@dataclass
class Question:
    qid: str
    domain: str
    qtype: str  # "single" or "multi"
    prompt: str
    options: Dict[str, str]  # letter -> text
    answer: Set[str]
    explanation: str = ""
    tags: str = ""


def _norm_letter(x: str) -> Optional[str]:
    x = (x or "").strip().upper()
    if not x:
        return None
    x = x.replace("(", "").replace(")", "").replace(".", "").replace(",", "").strip()
    if x in CHOICES:
        return x
    return None


def parse_answer(ans: str) -> Set[str]:
    ans = (ans or "").strip()
    if not ans:
        raise ValueError("Empty answer")
    parts = [p for p in ans.replace(",", ";").replace(" ", ";").split(";") if p.strip()]
    letters: Set[str] = set()
    for p in parts:
        l = _norm_letter(p)
        if not l:
            raise ValueError(f"Invalid answer letter: {p!r}")
        letters.add(l)
    return letters


def load_questions(path: str) -> List[Question]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"id", "domain", "type", "question", "A", "B", "C", "D", "answer"}
        if not reader.fieldnames:
            raise ValueError("CSV appears to have no header row.")
        missing = required - set(h.strip() for h in reader.fieldnames)
        if missing:
            raise ValueError(f"CSV missing required columns: {sorted(missing)}")

        qs: List[Question] = []
        for line_no, row in enumerate(reader, start=2):
            qtype = (row.get("type") or "").strip().lower()
            if qtype not in ("single", "multi"):
                raise ValueError(f"Row {line_no}: type must be 'single' or 'multi' (got {qtype!r})")

            options = {k: (row.get(k) or "").strip() for k in CHOICES}
            if any(not options[k] for k in CHOICES):
                raise ValueError(f"Row {line_no}: all options A-D must be non-empty")

            ans_set = parse_answer(row.get("answer") or "")
            if qtype == "single" and len(ans_set) != 1:
                raise ValueError(f"Row {line_no}: single-choice must have exactly 1 answer letter")
            if qtype == "multi" and len(ans_set) < 2:
                raise ValueError(f"Row {line_no}: multi-choice should have 2+ answer letters")

            qs.append(
                Question(
                    qid=(row.get("id") or "").strip(),
                    domain=(row.get("domain") or "").strip(),
                    qtype=qtype,
                    prompt=(row.get("question") or "").strip(),
                    options=options,
                    answer=ans_set,
                    explanation=(row.get("explanation") or "").strip(),
                    tags=(row.get("tags") or "").strip(),
                )
            )
        return qs


def list_domains(questions: List[Question]) -> None:
    domains = sorted({q.domain for q in questions if q.domain})
    print("\nAvailable domains:")
    for d in domains:
        count = sum(1 for q in questions if q.domain == d)
        print(f"  - {d} ({count} questions)")
    print()


def filter_by_domains(questions: List[Question], domains_csv: Optional[str]) -> List[Question]:
    if not domains_csv:
        return questions
    wanted = {d.strip().lower() for d in domains_csv.split(",") if d.strip()}
    if not wanted:
        return questions
    filtered = [q for q in questions if q.domain.strip().lower() in wanted]
    return filtered


def timed_input(prompt: str, timeout_s: int) -> Optional[str]:
    """
    Cross-platform timed input without external deps:
    - On Unix/macOS: uses signal alarm
    - On Windows: falls back to no-timeout (prints warning)
    """
    if timeout_s <= 0:
        return input(prompt)

    # Windows: no reliable signal.alarm
    if sys.platform.startswith("win"):
        print("⚠️ Timed input is limited on Windows in this simple version; running without timeout.")
        return input(prompt)

    import signal

    def handler(signum, frame):
        raise TimeoutError

    old_handler = signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_s)
    try:
        return input(prompt)
    except TimeoutError:
        return None
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


def ask_question(q: Question, time_per_q: Optional[int]) -> Tuple[bool, Set[str], float]:
    print("\n" + "-" * 78)
    header = f"[{q.domain}] Q{q.qid}" if q.qid else f"[{q.domain}]"
    if q.tags:
        header += f"  (tags: {q.tags})"
    print(header)
    print(q.prompt)
    print()
    for k in CHOICES:
        print(f"  {k}. {q.options[k]}")

    start = time.time()

    if q.qtype == "single":
        raw = timed_input("\nYour answer (A-D): ", time_per_q or 0)
        letter = _norm_letter(raw or "")
        user = {letter} if letter else set()
    else:
        raw = timed_input("\nYour answers (e.g., A;C): ", time_per_q or 0)
        try:
            user = parse_answer(raw) if raw and raw.strip() else set()
        except ValueError:
            user = set()

    elapsed = time.time() - start

    correct = user == q.answer
    if raw is None and time_per_q:
        print(f"⏱️ Time’s up ({time_per_q}s).")

    if correct:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect. Correct answer: {';'.join(sorted(q.answer))}")

    if q.explanation:
        print(f"   Explanation: {q.explanation}")

    return correct, user, elapsed


def weighted_sample(questions: List[Question], k: int) -> List[Question]:
    """
    Sample k questions with domain balancing:
    - tries to distribute questions across domains more evenly
    """
    if k >= len(questions):
        return questions[:]

    by_domain: Dict[str, List[Question]] = {}
    for q in questions:
        by_domain.setdefault(q.domain or "Unspecified", []).append(q)

    # Shuffle within each domain
    for dom in by_domain:
        random.shuffle(by_domain[dom])

    domains = list(by_domain.keys())
    random.shuffle(domains)

    picked: List[Question] = []
    # Round-robin pick across domains
    while len(picked) < k and any(by_domain[d] for d in domains):
        for d in domains:
            if len(picked) >= k:
                break
            if by_domain[d]:
                picked.append(by_domain[d].pop())
    return picked


def save_result(path: str, payload: dict) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="CCNP-friendly CSV quiz runner with domain selection.")
    p.add_argument("--csv", required=True, help="Path to quiz CSV file")
    p.add_argument("--list-domains", action="store_true", help="List domains in the CSV and exit")
    p.add_argument("--domains", default=None, help='Comma-separated domain list, e.g. "Infrastructure,Security"')
    p.add_argument("--shuffle", action="store_true", help="Shuffle question order")
    p.add_argument("--limit", type=int, default=None, help="Ask only N questions")
    p.add_argument("--time-per-q", type=int, default=None, help="Seconds allowed per question (Unix/macOS best)")
    p.add_argument("--weighted", action="store_true", help="If limiting, balance selection across domains")
    p.add_argument("--review-missed", action="store_true", help="Re-ask missed questions at the end")
    p.add_argument("--save", default=None, help="Append attempt results to JSONL file")
    args = p.parse_args(argv)

    try:
        questions = load_questions(args.csv)
    except Exception as e:
        print(f"Error loading CSV: {e}", file=sys.stderr)
        return 2

    if args.list_domains:
        list_domains(questions)
        return 0

    # Domain filter
    questions = filter_by_domains(questions, args.domains)
    if not questions:
        print("No questions matched your domain filter. Use --list-domains to see available names.")
        return 1

    # Shuffle / limit
    pool = questions[:]
    if args.shuffle and not args.limit:
        random.shuffle(pool)

    if args.limit is not None:
        if args.weighted:
            pool = weighted_sample(pool, args.limit)
        else:
            if args.shuffle:
                random.shuffle(pool)
            pool = pool[: args.limit]

    total = len(pool)
    correct = 0
    domain_stats: Dict[str, Dict[str, int]] = {}
    missed: List[Question] = []
    total_time = 0.0

    for q in pool:
        ok, user, elapsed = ask_question(q, args.time_per_q)
        total_time += elapsed

        domain_stats.setdefault(q.domain, {"correct": 0, "total": 0})
        domain_stats[q.domain]["total"] += 1
        if ok:
            correct += 1
            domain_stats[q.domain]["correct"] += 1
        else:
            missed.append(q)

    pct = (correct / total * 100) if total else 0.0

    print("\n" + "=" * 78)
    print(f"Score: {correct}/{total} ({pct:.1f}%)")
    print(f"Time:  {total_time:.1f}s total, {total_time/total:.1f}s/question" if total else "")
    print("\nPer-domain:")
    for dom in sorted(domain_stats.keys()):
        c = domain_stats[dom]["correct"]
        t = domain_stats[dom]["total"]
        dpct = (c / t * 100) if t else 0.0
        print(f"  - {dom}: {c}/{t} ({dpct:.1f}%)")
    print("=" * 78)

    if args.save:
        payload = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "csv": args.csv,
            "domains": args.domains,
            "limit": args.limit,
            "shuffle": args.shuffle,
            "weighted": args.weighted,
            "time_per_q": args.time_per_q,
            "score": {"correct": correct, "total": total, "pct": pct},
            "per_domain": domain_stats,
            "missed_count": len(missed),
            "seconds_total": total_time,
        }
        save_result(args.save, payload)
        print(f"Saved results to {args.save}")

    if args.review_missed and missed:
        print("\nReviewing missed questions...")
        # Re-ask in random order
        random.shuffle(missed)
        again_correct = 0
        for q in missed:
            ok, _, _ = ask_question(q, args.time_per_q)
            if ok:
                again_correct += 1
        print("\n" + "-" * 78)
        print(f"Review complete: {again_correct}/{len(missed)} corrected on retry.")
        print("-" * 78)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
