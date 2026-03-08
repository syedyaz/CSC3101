#!/usr/bin/env python3
"""
Quiz grader for Lecture 1 (Computer Architecture), Slides 1–24.
Reads answers.json and compares against the solution key.
Solution key is NOT in this file — it is supplied at run time (e.g. via
GitHub Actions secret QUIZ_ANSWERS) so students cannot see answers when
they clone the repo.
Exit code 0 = pass (>= 70%), non-zero = fail (for GitHub Actions).
"""

import json
import os
import sys
from pathlib import Path

PASS_PERCENT = 70  # Minimum score to pass (7/10)


def normalize(s: str) -> str:
    if s is None:
        return ""
    return str(s).strip().upper().replace(" ", "")


def load_solutions() -> dict:
    """Load solution key from environment (set in GitHub Actions from secret)."""
    raw = os.environ.get("QUIZ_ANSWERS")
    if not raw:
        return {}
    try:
        data = json.loads(raw)
        return {k: v for k, v in data.items() if k.startswith("Q") and k[1:].isdigit()}
    except json.JSONDecodeError:
        return {}


def main() -> int:
    solutions = load_solutions()
    if not solutions:
        print("Solutions are not available in this environment.")
        print("Push your answers to GitHub to run the automatic grader and see your score.")
        return 1

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
    total = len(solutions)
    wrong = []
    in_ci = os.environ.get("GITHUB_ACTIONS") == "true"

    for q, expected in solutions.items():
        raw = data.get(q, "")
        got = normalize(raw)
        exp_norm = normalize(expected)
        if got == exp_norm:
            correct += 1
        else:
            wrong.append((q, raw, expected))

    pct = (correct / total * 100) if total else 0
    passed = pct >= PASS_PERCENT

    # Write result for artifact (instructor can collect all into a table)
    result_path = Path(__file__).parent / "quiz_result.json"
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "score": correct,
                "total": total,
                "percentage": round(pct, 1),
                "passed": passed,
            },
            f,
            indent=2,
        )

    print(f"Score: {correct}/{total} ({pct:.0f}%)")
    if wrong:
        print("\nIncorrect questions:")
        for q, got, exp in wrong:
            if in_ci:
                # In GitHub Actions: do NOT show correct answer in the log
                print(f"  {q}: wrong (your answer: '{got}')")
            else:
                print(f"  {q}: your answer '{got}' -> correct '{exp}'")
    print("\nPASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
