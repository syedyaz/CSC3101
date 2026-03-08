# How to compile all quiz results into a table

Use the script **`collect_quiz_results.py`** to fetch every Grade Quiz run from GitHub and build one table (CSV + Markdown) for yourself.

---

## Step 1: Create a Personal Access Token (one-time)

1. On GitHub: your profile picture → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**.
2. **Generate new token (classic)**. Name it e.g. "Quiz results".
3. Enable scope: **repo** (read access is enough for public repos).
4. Generate and **copy the token** (you won't see it again).

---

## Step 2: Run the script

**Windows (PowerShell):**
```powershell
cd "C:\Users\Syed S Yazdani\Documents\Perso\SZABIST\Spring26\CA"
$env:GITHUB_TOKEN = "paste_your_token_here"
python collect_quiz_results.py syedyaz/CSC3101 --runs 50
```

**Mac/Linux:**
```bash
cd /path/to/CA
export GITHUB_TOKEN="paste_your_token_here"
python3 collect_quiz_results.py syedyaz/CSC3101 --runs 50
```

- Replace `paste_your_token_here` with your token.
- Replace `syedyaz/CSC3101` with your repo if different (e.g. `YourOrg/CSC3101`).
- `--runs 50` = last 50 workflow runs (increase if you have more submissions).

---

## Step 3: Open the results

The script creates two files in the same folder:

| File | Use |
|------|-----|
| **quiz_results.csv** | Open in Excel or Google Sheets. Columns: Student (GitHub), Run #, Score, Total, Pass, Date, Run URL. |
| **quiz_results.md** | Markdown table you can view or paste into a report. |

Each row is one submission (one push). **Student (GitHub)** is the GitHub username; **Score** and **Pass** come from the automatic grading.

---

## Note

You must push the updated workflow (with the "Upload quiz result" artifact step) so that each run produces an artifact. After that, run `collect_quiz_results.py` whenever you want an up-to-date table.
