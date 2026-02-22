Quick start

1) Put quiz_runner.py and your quiz CSV in the same folder.
2) Run:

   python quiz_runner.py --csv nvidia_ai_cert_quiz.csv
   python quiz_runner.py --csv nvidia_ai_cert_quiz.csv --shuffle
   python quiz_runner.py --csv nvidia_ai_cert_quiz.csv --shuffle --limit 10

CSV format

Header (required):
  id,section,type,question,A,B,C,D,answer

- type: single | multi
- answer:
    single: B
    multi: A;C

Tip: If you want more than 4 options, tell me and I’ll extend the format.
