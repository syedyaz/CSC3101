# Lecture 1 Quiz — Instructions for Students

**Course:** CSC3101 — Computer Architecture  
**Quiz:** 10 multiple-choice questions (Lecture 1, slides 1–24).  
**Submission:** Push your answers to GitHub. Your quiz is graded automatically; you do **not** submit on paper or email.

---

## Step 1: Get the quiz repo

**If the instructor gave you a link to clone (e.g. your own assignment repo):** use that link below instead of the one here.

Clone the repository to your computer:

```bash
git clone https://github.com/syedyaz/CSC3101.git
cd CSC3101
```

*(On Windows you can use **Git Bash** or **PowerShell**; on Mac/Linux use **Terminal**.)*

---

## Step 2: Answer the quiz

1. Open **`quiz_lecture1.md`** and read all 10 questions.
2. Open **`answers.json`** in any text editor (Notepad, VS Code, etc.).
3. Fill in your answers:
   - Optionally set `"student_name"` and `"student_id"` to your name and ID.
   - For each question, set the letter you choose: `"Q1": "A"`, `"Q2": "B"`, and so on up to `"Q10"`.
   - Use only **one letter per question**: `"A"`, `"B"`, `"C"`, or `"D"`.
   - Do not add extra spaces or change the structure of the file (keep it valid JSON).

**Example** (first two questions filled):

```json
{
  "student_name": "Ali Ahmed",
  "student_id": "12345",
  "Q1": "B",
  "Q2": "C",
  "Q3": "",
  ...
}
```

Fill all of Q1 through Q10, then save the file.

---

## Step 3: Push your answers to GitHub

In the same folder as the repo (where `answers.json` is), run:

```bash
git add answers.json
git commit -m "Submit Lecture 1 quiz answers"
git push origin main
```

If Git asks for your username and password:
- **Username:** your GitHub username  
- **Password:** use a **Personal Access Token**, not your GitHub password.  
  (Create one: GitHub → Settings → Developer settings → Personal access tokens → generate with `repo` scope.)

If your branch is called `master` instead of `main`, use:

```bash
git push origin master
```

---

## Step 4: See your result (pass/fail and score)

1. Open the repository on GitHub in your browser (e.g. **https://github.com/syedyaz/CSC3101** — or the repo URL your instructor gave you).
2. Click the **Actions** tab.
3. Click the **latest run** (the one from your push).
4. Click the **grade** job (left side or in the workflow diagram).
5. In the log you will see:
   - **Score: X/10 (Y%)**
   - **PASS** (green) if you got 7 or more correct (≥ 70%).
   - **FAIL** (red) if you got fewer than 7 correct; the log will list which question numbers were wrong.

You do **not** need to email or submit anything else; the grade is determined by this automated run.

---

## Summary

| Step | What to do |
|------|------------|
| 1 | Clone the repo (`git clone ...`, then `cd CSC3101`) |
| 2 | Open `quiz_lecture1.md` and answer; put your choices in `answers.json` (Q1–Q10 as "A"/"B"/"C"/"D") |
| 3 | Run: `git add answers.json` → `git commit -m "Submit Lecture 1 quiz answers"` → `git push origin main` |
| 4 | On GitHub, go to **Actions** → latest run → **grade** job to see your score and PASS/FAIL |

---

**Need help?** Ask your instructor. Include the repo URL and the **Actions** run link if your push or result does not appear as expected.
