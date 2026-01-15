### 🧾 Git Cheat Sheet (For Daily Use & Interviews)
### 🔹 1. Git Setup (One-Time)
Check Git version
git --version

Configure user
git config --global user.name "Your Name"
git config --global user.email "youremail@gmail.com"

Check config
git config --list

### 🔹 2. Starting a Repository
Initialize Git
git init

Clone existing repo
git clone <repo-url>

### 🔹 3. Basic Workflow (MOST IMPORTANT)
Check file status
git status

Add files
git add file_name
git add .

Commit changes
git commit -m "meaningful message"

Push to GitHub
git push

### 🔹 4. Connecting to GitHub
Add remote
git remote add origin <repo-url>

Verify remote
git remote -v

First push
git push -u origin main

### 🔹 5. Branching (Basics)
Check branches
git branch

Create new branch
git branch branch_name

Switch branch
git checkout branch_name

Create + switch
git checkout -b branch_name

### 🔹 6. Pulling & Syncing
Pull latest changes
git pull

Fetch without merge
git fetch

### 🔹 7. Viewing History
Commit history
git log

One-line history
git log --oneline

### 🔹 8. Undoing Mistakes (IMPORTANT)
Unstage file
git restore --staged file_name

Discard local changes
git restore file_name

Amend last commit
git commit --amend

### 🔹 9. Stashing Changes
Save work temporarily
git stash

Apply stash
git stash apply

List stashes
git stash list

### 🔹 10. Deleting & Renaming
Delete file
git rm file_name

Rename file
git mv old_name new_name

### 🔹 11. .gitignore (VERY IMPORTANT)

Example:

venv/
__pycache__/
.ipynb_checkpoints/
.env

### 🔹 12. Daily Git Routine (BEST PRACTICE)
git status
git add .
git commit -m "Day XX: what I learned"
git push

### 🔹 13. Interview-Ready One-Liners

Git → Version control system

GitHub → Code hosting platform

Commit → Snapshot of code

Branch → Independent line of development

Merge → Combine branches

Pull → Fetch + merge changes

Clone → Copy repo locally