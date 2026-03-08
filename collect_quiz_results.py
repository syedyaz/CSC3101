#!/usr/bin/env python3
"""
Collect quiz results from GitHub Actions runs into a single table (CSV + Markdown).

Usage:
  1. Create a Personal Access Token (GitHub → Settings → Developer settings
     → Personal access tokens) with scope: repo, actions (read).
  2. Set it:  set GITHUB_TOKEN=your_token   (Windows)  or  export GITHUB_TOKEN=your_token   (Mac/Linux)
  3. Run:     python collect_quiz_results.py [owner/repo] [--runs N]

  Example: python collect_quiz_results.py syedyaz/CSC3101 --runs 50

Output: quiz_results.csv and quiz_results.md in the current directory.
"""

import argparse
import csv
import json
import os
import sys
import zipfile
from io import BytesIO
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def api_get(token: str, url: str) -> dict | list:
    req = Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    with urlopen(req) as resp:
        return json.loads(resp.read().decode())


def api_download(token: str, url: str) -> bytes:
    req = Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urlopen(req) as resp:
        return resp.read()


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect quiz results from GitHub Actions")
    parser.add_argument("repo", nargs="?", default="syedyaz/CSC3101", help="Owner/repo, e.g. syedyaz/CSC3101")
    parser.add_argument("--runs", type=int, default=30, help="Max number of workflow runs to fetch (default 30)")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("ERROR: Set GITHUB_TOKEN (Personal Access Token with repo + actions read).", file=sys.stderr)
        return 1

    owner, repo = args.repo.split("/", 1)
    base = f"https://api.github.com/repos/{owner}/{repo}"

    # Find Grade Quiz workflow
    workflows = api_get(token, f"{base}/actions/workflows")
    workflow_id = None
    for w in workflows.get("workflows", []):
        if w.get("path", "").endswith("grade-quiz.yml") or "Grade Quiz" in (w.get("name") or ""):
            workflow_id = w["id"]
            break
    if not workflow_id:
        print("ERROR: No Grade Quiz workflow found.", file=sys.stderr)
        return 1

    # List workflow runs
    runs = api_get(
        token,
        f"{base}/actions/workflows/{workflow_id}/runs?per_page={min(args.runs, 100)}"
    )
    run_list = runs.get("workflow_runs", [])
    if not run_list:
        print("No workflow runs found.")
        return 0

    rows = []
    for run in run_list:
        run_id = run["id"]
        run_number = run["run_number"]
        actor = run.get("actor", {}).get("login") or run.get("actor", {}).get("login") or "?"
        conclusion = run.get("conclusion") or "?"
        created = (run.get("created_at") or "")[:19].replace("T", " ")

        # Get artifacts for this run
        artifacts_url = run.get("artifacts_url")
        if not artifacts_url:
            row = {"Student (GitHub)": actor, "Run #": run_number, "Score": "—", "Total": 10, "Pass": conclusion == "success", "Date": created, "Run URL": run.get("html_url", "")}
            rows.append(row)
            continue

        try:
            arts = api_get(token, artifacts_url)
        except (HTTPError, URLError):
            row = {"Student (GitHub)": actor, "Run #": run_number, "Score": "—", "Total": 10, "Pass": conclusion == "success", "Date": created, "Run URL": run.get("html_url", "")}
            rows.append(row)
            continue

        art_list = arts.get("artifacts", [])
        quiz_artifact = None
        for a in art_list:
            if a.get("name", "").startswith("quiz-result-"):
                quiz_artifact = a
                break

        if not quiz_artifact:
            row = {"Student (GitHub)": actor, "Run #": run_number, "Score": "—", "Total": 10, "Pass": conclusion == "success", "Date": created, "Run URL": run.get("html_url", "")}
            rows.append(row)
            continue

        # Download artifact (zip)
        archive_url = quiz_artifact.get("archive_download_url")
        if not archive_url:
            row = {"Student (GitHub)": actor, "Run #": run_number, "Score": "—", "Total": 10, "Pass": conclusion == "success", "Date": created, "Run URL": run.get("html_url", "")}
            rows.append(row)
            continue

        try:
            zip_data = api_download(token, archive_url)
        except (HTTPError, URLError):
            row = {"Student (GitHub)": actor, "Run #": run_number, "Score": "—", "Total": 10, "Pass": conclusion == "success", "Date": created, "Run URL": run.get("html_url", "")}
            rows.append(row)
            continue

        try:
            with zipfile.ZipFile(BytesIO(zip_data), "r") as z:
                names = z.namelist()
                if "quiz_result.json" in names:
                    with z.open("quiz_result.json") as f:
                        data = json.load(f)
                    score = data.get("score", "—")
                    total = data.get("total", 10)
                    passed = data.get("passed", conclusion == "success")
                else:
                    score, total, passed = "—", 10, conclusion == "success"
        except (zipfile.BadZipFile, KeyError, json.JSONDecodeError):
            score, total, passed = "—", 10, conclusion == "success"

        row = {
            "Student (GitHub)": actor,
            "Run #": run_number,
            "Score": score,
            "Total": total,
            "Pass": "Yes" if passed else "No",
            "Date": created,
            "Run URL": run.get("html_url", ""),
        }
        rows.append(row)

    if not rows:
        print("No results to write.")
        return 0

    # Sort by run number descending (latest first)
    rows.sort(key=lambda r: (r.get("Run #") or 0), reverse=True)

    # CSV
    csv_path = "quiz_results.csv"
    fieldnames = ["Student (GitHub)", "Run #", "Score", "Total", "Pass", "Date", "Run URL"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {csv_path} ({len(rows)} rows).")

    # Markdown table
    md_path = "quiz_results.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Quiz results (Lecture 1)\n\n")
        f.write("| Student (GitHub) | Run # | Score | Total | Pass | Date |\n")
        f.write("|------------------|-------|-------|-------|------|------|\n")
        for r in rows:
            f.write(f"| {r['Student (GitHub)']} | {r['Run #']} | {r['Score']} | {r['Total']} | {r['Pass']} | {r['Date']} |\n")
    print(f"Wrote {md_path}.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
