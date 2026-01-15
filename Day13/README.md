# Day 13 – Environment Setup & Git 🧠⚙️

Today was one of the **most important foundational days** of my AI/ML journey.  I'm already following this since day 1
Instead of jumping into algorithms, I focused on **setting up a clean development environment** and Mentioning everything about **Git & GitHub**, which are essential for real-world ML projects.

---

## 🔹 Why Environment Setup Matters in AI/ML

AI/ML projects require:
- Specific Python versions
- Different library versions (NumPy, Pandas, TensorFlow, etc.)
- Isolation to avoid breaking other projects

That’s why **virtual environments** are critical.

---

## 🟢 Conda & Virtual Environments

### 🔸 What is Conda?
Conda is a **package and environment manager** that helps:
- Install Python and libraries easily
- Create isolated environments
- Avoid dependency conflicts

but i am using Python venv (Lightweight & Built-in)

### 🔸 Why use Virtual Environments?
Each project can have:
- Its own Python version
- Its own libraries
- Zero interference with other projects

---

### 🛠 Creating a Conda Environment (Practiced)

```bash
conda create -n ai_ml_env python=3.10
### What I did?

### 🔹 Python venv (Lightweight & Built-in)

Even if you’re not using Conda, venv is strongly recommended.

Create virtual environment
python -m venv venv

Activate (Windows)
venv\Scripts\activate

Activate (Mac/Linux)
source venv/bin/activate

Verify
python --version
pip list

### 🟢 VS Code Integration (Very Important)

Open your project folder in VS Code

Press Ctrl + Shift + P

Select Python: Select Interpreter

Choose:

./venv/Scripts/python.exe

Now:

Jupyter

Notebooks

Python scripts

### 👉 All use the same environment

### 📦 Libraries You’ll Need (Days 13–17)(we've already used most of them)

Install once inside venv:

pip install numpy pandas matplotlib seaborn jupyter

(Optional but useful later)

pip install scikit-learn

### 📁 Repo Structure (No Conda Version)
Data-Science-Tools-Setup/
│
├── venv/   ❌ (ignored in git)
│
├── Day13_Environment_Git/
│   ├── Task.md
│   └── README.md
│
├── Day14_Python_DS/
├── Day15_NumPy/
├── Day16_Pandas/
├── Day17_Data_Visualization/
│
└── .gitignore

### 🟢 GitHub Workflow (for now we only need these cmds)
1️⃣ Initialize Git
git init

2️⃣ Check status
git status

3️⃣ Add files
git add .

4️⃣ Commit changes
git commit -m "Day 13: Environment setup and Git basics"

5️⃣ Connect to GitHub
git remote add origin <repository-url>

6️⃣ Push code
git push -u origin main

### 🟢 Git Basics (Version Control)
### 🔸 What is Git?

Git is a version control system that:

Tracks code changes

Helps revert mistakes

Enables collaboration

### 🔸 Why Git is essential for ML?

Track experiments

Manage dataset changes

Collaborate with teams

Maintain clean project history

### 📓 Jupyter Notebook / JupyterLab

Jupyter is one of the most important tools in Data Science and Machine Learning. It allows combining code, output, text, and visualizations in a single interactive document.

### 🟢 What is Jupyter Notebook?

Jupyter Notebook is an interactive computing environment where you can:

Write Python code in cells

Execute code step by step

See output instantly

Add explanations using Markdown

Visualize data easily

It is widely used for:

Data exploration

Data cleaning

Machine learning experiments

Teaching & research

### 🟢 What is JupyterLab?

JupyterLab is the next-generation interface of Jupyter Notebook.

It provides:

Multiple notebooks in tabs

File browser

Integrated terminal

Better UI & productivity

### 👉 Think of it as Notebook + IDE features.

### 🔍 Jupyter Notebook vs JupyterLab
Feature	Jupyter Notebook	JupyterLab
Interface	Simple	Advanced
Multiple files	Limited	Yes
Terminal	No	Yes
Best for	Beginners	Advanced workflows
### 🛠 Using Jupyter in VS Code (My Setup)

Since you’re using VS Code, you don’t need browser-based Jupyter.

- ✔ Required VS Code Extensions

Python

Jupyter

VS Code handles everything internally.

▶ Creating a Notebook in VS Code

Open VS Code

Ctrl + Shift + P

Select Jupyter: Create New Blank Notebook

Choose Python kernel (your venv)

File saved as:

example.ipynb

### 🧪 Cell Types (Very Important)
### 🔹 Code Cell

Used to write and run Python code.

```python
print("Hello Jupyter")

```
### 🔹 Markdown Cell

Used to explain concepts.

## This is a markdown heading

### 👉 Best practice:
Explain → Code → Output

▶ Running Cells

Shift + Enter → Run & move next

Ctrl + Enter → Run only

Alt + Enter → Run & add new cell

### 📊 Why Jupyter is Perfect for Data Science

- ✔ Interactive experimentation
- ✔ Easy debugging
- ✔ Visualization support
- ✔ Clean documentation
- ✔ Notebook-based ML workflows

### 🧠 Best Practices (Very Important)

- ✔ Keep cells small & focused
- ✔ Use Markdown to explain logic
- ✔ Run notebooks top-to-bottom before committing
- ✔ Save outputs (recruiters like this)
- ✔ Use meaningful file names

### 🆚 Jupyter vs Python Scripts
Notebook	Script
Interactive	Linear
Great for learning	Great for production
Visual outputs	No inline plots

### 👉 In DS/ML:

Learn & explore → Notebook

Deploy → Python scripts

### 📌 How This Fits in Your AI/ML Challenge

Day 13: Learn Jupyter basics

Days 14–17: Use notebooks daily

GitHub: Push .ipynb with outputs

Interviews: Explain workflow confidently

✅ Summary

Jupyter Notebook / JupyterLab is a core Data Science tool that makes learning, experimenting, and explaining ML concepts easier.
Using it inside VS Code + venv is a professional and industry-accepted setup.