#!/usr/bin/env python3
"""
quiz_runner.py — Simple CSV-driven quiz app (CLI)

CSV format (required columns):
  id, section, type, question, A, B, C, D, answer
Optional:
  explanation

- type: "single" or "multi"
- answer:
    single -> "B"
    multi  -> "A;C"   (semicolon-separated letters, order-insensitive)

Usage:
  python quiz_runner.py --csv nvidia_ai_cert_quiz.csv
  python quiz_runner.py --csv myquiz.csv --shuffle --limit 10
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple


CHOICES = ("A", "B", "C", "D")


@dataclass
class Question:
    qid: str
    section: str
    qtype: str  # "single" or "multi"
    prompt: str
    options: Dict[str, str]  # letter -> text
    answer: Set[str]         # set of letters
    explanation: str = ""


def _norm_letter(x: str) -> Optional[str]:
    x = (x or "").strip().upper()
    if not x:
        return None
    # accept "a", "A.", "(A)", etc.
    x = x.replace("(", "").replace(")", "").replace(".", "").replace(",", "").strip()
    if x in CHOICES:
        return x
    return None


def parse_answer(ans: str) -> Set[str]:
    ans = (ans or "").strip()
    if not ans:
        raise ValueError("Empty answer")
    # allow separators ; , space
    parts = [p for p in ans.replace(",", ";").replace(" ", ";").split(";") if p.strip()]
    letters = set()
    for p in parts:
        l = _norm_letter(p)
        if not l:
            raise ValueError(f"Invalid answer letter: {p!r}")
        letters.add(l)
    return letters


def load_questions(path: str) -> List[Question]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"id", "section", "type", "question", "A", "B", "C", "D", "answer"}
        if not reader.fieldnames:
            raise ValueError("CSV appears to have no header row.")
        missing = required - set(h.strip() for h in reader.fieldnames)
        if missing:
            raise ValueError(f"CSV missing required columns: {sorted(missing)}")

        qs: List[Question] = []
        for i, row in enumerate(reader, start=2):
            qtype = (row.get("type") or "").strip().lower()
            if qtype not in ("single", "multi"):
                raise ValueError(f"Row {i}: type must be 'single' or 'multi' (got {qtype!r})")

            options = {k: (row.get(k) or "").strip() for k in CHOICES}
            if any(not options[k] for k in CHOICES):
                raise ValueError(f"Row {i}: all options A-D must be non-empty")

            ans_set = parse_answer(row.get("answer") or "")
            if qtype == "single" and len(ans_set) != 1:
                raise ValueError(f"Row {i}: single-choice must have exactly 1 answer letter")
            if qtype == "multi" and len(ans_set) < 2:
                raise ValueError(f"Row {i}: multi-choice should have 2+ answer letters")

            qs.append(
                Question(
                    qid=(row.get("id") or "").strip(),
                    section=(row.get("section") or "").strip(),
                    qtype=qtype,
                    prompt=(row.get("question") or "").strip(),
                    options=options,
                    answer=ans_set,
                    explanation=(row.get("explanation") or "").strip(),
                )
            )
        return qs


def ask_question(q: Question, show_answer: bool = True) -> Tuple[bool, Set[str]]:
    print("\n" + "-" * 72)
    header = f"[{q.section}] Q{q.qid}" if q.qid else f"[{q.section}]"
    print(header)
    print(q.prompt)
    print()
    for k in CHOICES:
        print(f"  {k}. {q.options[k]}")

    if q.qtype == "single":
        raw = input("\nYour answer (A-D): ").strip()
        letter = _norm_letter(raw)
        user = {letter} if letter else set()
    else:
        raw = input("\nYour answers (e.g., A;C): ").strip()
        # parse like answer, but allow empty -> {}
        try:
            user = parse_answer(raw) if raw.strip() else set()
        except ValueError:
            user = set()

    correct = user == q.answer
    if show_answer:
        if correct:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. Correct answer: {';'.join(sorted(q.answer))}")
        if q.explanation:
            print(f"   Explanation: {q.explanation}")
    return correct, user


def run_quiz(questions: List[Question], shuffle: bool, limit: Optional[int]) -> int:
    qs = questions[:]
    if shuffle:
        random.shuffle(qs)
    if limit is not None:
        qs = qs[:limit]

    correct = 0
    for q in qs:
        ok, _ = ask_question(q)
        if ok:
            correct += 1

    total = len(qs)
    pct = (correct / total * 100) if total else 0.0
    print("\n" + "=" * 72)
    print(f"Score: {correct}/{total} ({pct:.1f}%)")
    print("=" * 72)
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="CSV-driven quiz runner (CLI).")
    p.add_argument("--csv", required=True, help="Path to quiz CSV file")
    p.add_argument("--shuffle", action="store_true", help="Shuffle question order")
    p.add_argument("--limit", type=int, default=None, help="Ask only the first N questions (after shuffle)")
    args = p.parse_args(argv)

    try:
        questions = load_questions(args.csv)
    except Exception as e:
        print(f"Error loading CSV: {e}", file=sys.stderr)
        return 2

    return run_quiz(questions, shuffle=args.shuffle, limit=args.limit)


if __name__ == "__main__":
    raise SystemExit(main())
