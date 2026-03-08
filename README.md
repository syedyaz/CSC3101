# CSC3101 — Lecture 1 Quiz (Computer Architecture, Slides 1–24)

10 multiple-choice questions based on **Lecture-1.pdf** (slides 1 to 24 only).  
The quiz is graded automatically on GitHub when students push or open a pull request.

---

## What’s in this repo

| File / folder | Purpose |
|---------------|--------|
| `quiz_lecture1.md` | Quiz questions (10 MCQs). Students read this. |
| `answers.json` | **Students edit this** — they set Q1–Q10 to "A", "B", "C", or "D". |
| `grader.py` | Script that checks `answers.json`; solution key is **not** in the repo (supplied via GitHub secret). |
| `.github/workflows/grade-quiz.yml` | GitHub Action that runs the grader on every push/PR. |
| `Lecture-1.pdf` | Lecture slides (reference). |

---

## For the instructor: put the quiz on GitHub

### 1. Create a new repository on GitHub

- Go to [github.com/new](https://github.com/new).
- Choose a name (e.g. `ca-lecture1-quiz`), set Public, then **Create repository**.

### 2. Push this folder to the new repo

From your machine, in the folder that contains `quiz_lecture1.md`, `answers.json`, `grader.py`, and `.github/`:

```bash
cd "C:\Users\Syed S Yazdani\Documents\Perso\SZABIST\Spring26\CA"

git init
git add quiz_lecture1.md answers.json grader.py .github/ README.md
git add Lecture-1.pdf
git commit -m "Add Lecture 1 quiz (10 MCQs, slides 1-24) and auto-grader"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your GitHub username and repo name.

### 3. Add the solution key as a secret (students cannot see answers)

The correct answers are **not** in the repo. You store them in a GitHub secret so that:
- Grading still works when students push (Actions has access to the secret).
- Students cannot see the solutions when they clone the repo.

1. On GitHub, open your repo → **Settings** → **Secrets and variables** → **Actions**.
2. Click **New repository secret**.
3. **Name:** `QUIZ_ANSWERS`
4. **Value:** a single-line JSON object with the correct answers, for example:
   ```json
   {"Q1":"B","Q2":"C","Q3":"C","Q4":"A","Q5":"B","Q6":"C","Q7":"D","Q8":"B","Q9":"B","Q10":"B"}
   ```
   Replace the values with your actual correct answers (A/B/C/D for each Q1–Q10). No spaces. Save the secret.

If you use **GitHub Classroom**: add the same secret at the **organization** level (Settings → Secrets and variables → Actions) so all student assignment repos can use it.

### 4. Confirm automatic grading

- Open the repo on GitHub → **Actions** tab.
- You should see the workflow **Grade Quiz**. It runs on every push and pull request to `main` (or `master`).
- Push a commit with correct answers in `answers.json` and confirm the workflow turns green (PASS).

---

## For students: take the quiz on GitHub

### Option A: Clone, answer, push (individual work)

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_INSTRUCTOR_REPO/REPO_NAME.git
   cd REPO_NAME
   ```

2. **Read the questions**  
   Open `quiz_lecture1.md` and answer all 10 MCQs.

3. **Submit your answers**  
   Edit `answers.json`:
   - Set `student_name` and `student_id` (optional but recommended).
   - For each question, set the correct key to the letter you choose, e.g.:
     - `"Q1": "B"`
     - `"Q2": "C"`
     - … up to `"Q10": "A"` (or whatever your answers are).

4. **Check locally (optional)**  
   Run the grader on your machine:
   ```bash
   python grader.py
   ```
   You’ll see your score and which answers are wrong — the solution key is not in the repo, so your score is only shown when you push to GitHub.

5. **Push to GitHub**  
   ```bash
   git add answers.json
   git commit -m "Submit Lecture 1 quiz answers"
   git push
   ```

6. **See the result**  
   Go to the repo on GitHub → **Actions** tab. Open the latest run. The **Grade Quiz** job will show:
   - **PASS** (green) if score ≥ 70% (7/10).
   - **FAIL** (red) if score &lt; 70%; the log shows which questions were wrong.

### Option B: Fork and pull request

1. **Fork** the instructor’s repo to your GitHub account.
2. **Clone your fork** and make the same edits to `answers.json` as in Option A.
3. **Push** to your fork, then open a **Pull request** from your branch to the instructor’s `main`.
4. The **Grade Quiz** workflow runs on the pull request; the check appears on the PR page (pass/fail and score in the Actions log).

---

## How automatic checking works

- On every **push** or **pull request** to the default branch (`main` or `master`), GitHub runs the workflow in `.github/workflows/grade-quiz.yml`.
- The workflow:
  1. Checks out the repo.
  2. Runs `python grader.py`.
  3. The grader reads `answers.json`, compares each Q1–Q10 to the solution key, and prints the score.
  4. If score **≥ 70%** (7/10): the workflow step exits with 0 → **PASS**.
  5. If score **&lt; 70%**: the step exits with 1 → **FAIL**; the log lists which questions were incorrect.

So: **automatic checking = GitHub Actions runs `grader.py` and uses its exit code to show pass/fail.**

---

## Pass criteria

- **Pass:** 7 or more correct out of 10 (≥ 70%).
- **Fail:** Fewer than 7 correct.

To change the pass threshold, edit `PASS_PERCENT` in `grader.py` (e.g. `80` for 80%).
