#!/usr/bin/env python3
"""
Quiz grader for Lecture 1 (Computer Architecture), Slides 1–24.
Reads answers.json and compares against the solution key.
Exit code 0 = pass (>= 70%), non-zero = fail (for GitHub Actions).
"""

import json
import sys
from pathlib import Path

# Solution key for 10 MCQs (Q1–Q10)
SOLUTIONS = {
    "Q1": "B",
    "Q2": "C",
    "Q3": "C",
    "Q4": "A",
    "Q5": "B",
    "Q6": "C",
    "Q7": "D",
    "Q8": "B",
    "Q9": "B",
    "Q10": "B",
}

PASS_PERCENT = 70  # Minimum score to pass (7/10)


def normalize(s: str) -> str:
    if s is None:
        return ""
    return str(s).strip().upper().replace(" ", "")


def main() -> int:
    answers_path = Path(__file__).parent / "answers.json"
    if not answers_path.exists():
        print("ERROR: answers.json not found. Create it from the template.")
        return 1

    try:
        with open(answers_path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in answers.json: {e}")
        return 1

    correct = 0
    total = len(SOLUTIONS)
    wrong = []

    for q, expected in SOLUTIONS.items():
        if q in ("student_name", "student_id"):
            continue
        raw = data.get(q, "")
        got = normalize(raw)
        exp_norm = normalize(expected)
        if got == exp_norm:
            correct += 1
        else:
            wrong.append((q, raw, expected))

    pct = (correct / total * 100) if total else 0
    passed = pct >= PASS_PERCENT

    print(f"Score: {correct}/{total} ({pct:.0f}%)")
    if wrong:
        print("\nIncorrect:")
        for q, got, exp in wrong:
            print(f"  {q}: your answer '{got}' -> correct '{exp}'")
    print("\nPASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
