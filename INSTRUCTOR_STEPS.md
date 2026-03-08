# Step-by-step: Automated quiz checking (no manual grading)

Follow these steps once. After that, every student push is graded automatically and you only check **pass/fail** and **score** on GitHub.

---

## Part A: One-time setup (you do this once)

### Step 1: Make sure the quiz repo is on GitHub

You already have the repo at `https://github.com/syedyaz/CSC3101`. If the latest code (grader, workflow, quiz files) is there, skip to Step 2.

If you still need to push from your machine:

```powershell
cd "C:\Users\Syed S Yazdani\Documents\Perso\SZABIST\Spring26\CA"
git add .
git status
git commit -m "Quiz and auto-grader"
git push origin main
```

### Step 2: Add the solution key as a secret (required for auto-grading)

Without this secret, the grader cannot run and students will see “Solutions are not available.”

1. Open **https://github.com/syedyaz/CSC3101**
2. Click **Settings** (repo settings, not your profile).
3. In the left sidebar, click **Secrets and variables** → **Actions**.
4. Click **New repository secret**.
5. **Name:** type exactly: `QUIZ_ANSWERS`
6. **Value:** paste this (one line, no line breaks), then click **Add secret**:

   ```
   {"Q1":"B","Q2":"C","Q3":"C","Q4":"A","Q5":"B","Q6":"C","Q7":"D","Q8":"B","Q9":"B","Q10":"B"}
   ```

   *(If your correct answers differ, change the letters for Q1–Q10 in that JSON.)*

### Step 3: Confirm the workflow runs

1. In the repo, go to the **Actions** tab.
2. You should see a workflow named **Grade Quiz**.
3. Open the latest run (or trigger one by pushing a commit).
4. Open the **grade** job. You should see output like:
   - `Score: 10/10 (100%)` and `PASS` if answers are correct,
   - or `Score: 6/10 (60%)` and `FAIL` plus a list of wrong questions.

If you see **PASS** or **FAIL** and a score, automated checking is working. You do **not** need to grade by hand.

---

## Part B: How students submit (share this with students)

1. **Clone the repo**
   ```bash
   git clone https://github.com/syedyaz/CSC3101.git
   cd CSC3101
   ```

2. **Answer the quiz**  
   Open `quiz_lecture1.md` for questions. Edit `answers.json` and set `"Q1"` through `"Q10"` to their chosen letter (e.g. `"Q1": "B"`).

3. **Push to GitHub**
   ```bash
   git add answers.json
   git commit -m "Quiz answers"
   git push origin main
   ```

   *(If they use a fork or their own branch, they push there and can open a Pull Request to your repo.)*

---

## Part C: How you see results (no manual checking)

Grading is **fully automatic**. You only look at GitHub; you do not run the grader yourself.

### Option 1: One repo shared by all students (e.g. everyone pushes to main)

- Go to **Actions** tab: **https://github.com/syedyaz/CSC3101/actions**
- Each run is one submission (one push).
- Click a run → click the **grade** job.
- In the log you will see:
  - **Score: X/10 (Y%)** and **PASS** or **FAIL**
  - If FAIL, which question numbers were wrong (e.g. `Q1: wrong (your answer: 'A')`).

To record grades: note the commit author (or branch) and the score/PASS/FAIL from that run.

### Option 2: Each student has their own repo (e.g. GitHub Classroom)

- Each student’s repo has its own **Actions** tab.
- When they push, **Grade Quiz** runs in their repo.
- You can:
  - Open each student repo → **Actions** → latest run → **grade** job to see score and PASS/FAIL, or
  - Use a dashboard/script that lists recent workflow runs across repos (optional).

In both options, **you do not run the grader manually**; GitHub Actions runs it on every push and shows the result in the run log.

---

## Quick reference

| You want to…                    | What to do |
|---------------------------------|------------|
| Enable auto-grading             | Add secret `QUIZ_ANSWERS` (Step 2). |
| See if a submission passed      | Repo → **Actions** → open latest run → **grade** job → read PASS/FAIL and score. |
| Change pass threshold (e.g. 80%)| Edit `PASS_PERCENT` in `grader.py` (e.g. to `80`) and push. |
| Change correct answers          | Edit the `QUIZ_ANSWERS` secret in Settings → Secrets and variables → Actions. |
| Compile all results into a table | Run `python collect_quiz_results.py syedyaz/CSC3101` (see Part D below). |

Once the secret is set and one run shows a score and PASS/FAIL, checking is automated and you don’t need to check the quiz manually.
