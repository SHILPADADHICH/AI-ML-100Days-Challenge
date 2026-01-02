# Day 01 – Python Setup & Environment

---

## Python Installation

Python 3 (current version): This is what you’ll learn and use. Check the versions here.  
Python 2 (outdated): Stopped being supported in 2020. You might see old code mentioning it, but ignore it – it’s like using Windows XP.

I have already Python installed in my Windows.  
You can follow any tutorial for that.

---

## Code Editor – VS Code

For code editor I am using VS Code because:

VS Code is technically a “code editor” but with extensions, it becomes a full IDE.

---

## Install Python Extension

VS Code needs the Python extension to work properly with Python files:

- Click the Extensions icon in the left sidebar (it looks like 4 squares)
- Search for “Python”
- Find the one by Microsoft (it has millions of downloads)

---

## Configure Python Execution

After installing the Python extension, enable this important setting:

- Open Settings (Ctrl/Cmd + ,)
- Search for “Python Terminal Execute In File Dir”
- Check the box to enable it

---

## Additional Recommended Extensions

While VS Code works great with just the Python extension, here are a few more I recommend:

### Pylance
- Search for “Pylance” by Microsoft  
- Provides even better code completion and error detection  
- Works alongside the Python extension  

### Jupyter
- Search for “Jupyter” by Microsoft  
- Enables interactive Python mode (we’ll use this later)  
- Essential for data science and AI work  

---

## Git Basics

You should know how to use git cmds and atleast basic ones:
- how to create directory
- push code

---

## File Extensions

File extensions tell your computer and VS Code what type of file you’re working with.  
There are many file types, here are some examples:

- `.txt` – Plain text file, no special formatting  
- `.md` – Markdown file, for documentation  
- `.py` – Python file, contains Python code  

---

## Project Structure

In root directory (100 days challenge):

Create your `Day01` directory.

In this, create files you will be working on.

---

## Write Your First Program

In your `hello.py` file, type:

```python
print("Hello, World!")
print("I'm learning Python for AI")


## Run Your Program

There are ways to run your Python code:

### Method 1: Run button (easiest)
Click the triangle “Run” button in the top-right corner  
Or select the down arrow next to it and select “Run Python File”

### Method 2: Right-click menu
Right-click anywhere in your code  
Select “Run Python File in Terminal”

### In terminal:
```bash
python hello.py

