### 📘 Day 14 – Jupyter Mastery (Detailed Explanation)
### 🔹 1. Lecture: Jupyter Notebooks & Magic Commands (1 hour)
✅ What is Jupyter Notebook?

Jupyter Notebook is an interactive computing environment where you can:

Write code

Run it step by step

See outputs instantly

Add explanations using Markdown

In AI/ML, Jupyter is used for:

Data exploration

Experimentation

Model training

Research documentation

### 🧩 Cell Types

Code Cell

Runs Python code

Markdown Cell

Used for headings, explanations, formulas, notes

### 👉 Good notebooks mix code + explanation.

⚙️ Kernel & Execution Order

```python
Kernel = Python engine running in the background

```
Cells execute in the order you run them, not top-to-bottom automatically

- ⚠️ Common mistake:
Using variables defined in a cell that wasn’t executed → error or wrong output.

✨ Magic Commands (Very Important)

Magic commands make notebooks powerful.

### 🔹 Line Magics (%)

Work on a single line.

%time sum(range(1000000))

➡️ Tells how long execution took.

%matplotlib inline

➡️ Displays plots inside notebook.

### 🔹 Cell Magics (%%)

Apply to entire cell.

%%time
```python
total = 0
for i in range(1000000):
```
total += i

### 🔹 Auto Reload (Super useful)
%load_ext autoreload
%autoreload 2

➡️ Automatically reloads Python files when modified (used in ML projects).

### 🧠 Why this matters?

In real ML work:

You constantly tweak code

You need fast feedback

Magic commands save time + mental effort

### 🔹 2. Coding: Interactive Notebook Widgets (2 hours)
✅ What are widgets?

Widgets allow user interaction inside notebooks (sliders, buttons, dropdowns).

Used in:

Hyperparameter tuning

Visualization

Demos

### 📦 Installation
pip install ipywidgets

### 🎚 Example 1: Slider Widget
```python
import ipywidgets as widgets
from IPython.display import display

slider = widgets.IntSlider(value=5, min=0, max=10)
```
display(slider)

➡️ You can change values without rerunning code manually.

### 🔽 Example 2: Dropdown Widget
```python
dropdown = widgets.Dropdown(
```
options=['Linear Regression', 'Decision Tree', 'SVM'],
description='Model:'
)
display(dropdown)

### 🔁 Example 3: Interactive Function
```python
def square(x):
    return x * x

```
widgets.interact(square, x=(0, 10))

➡️ Changing slider updates output automatically.

### 🧠 Why widgets matter in ML?

Real-time parameter tuning

Faster experimentation

Better understanding of model behavior

### 🔹 3. Practice: Best Practices for Research Notebooks (1 hour)
- ❌ Bad Notebook

No headings

Random cells

Hardcoded values

No explanation

✅ Good Research Notebook Structure

Title & Objective

# House Price Prediction
Objective: Predict house prices using regression

Imports

```python
import numpy as np
import pandas as pd

```
Configuration

```python
RANDOM_STATE = 42
TEST_SIZE = 0.2

```
Functions

```python
def clean_data(df):
    return df.dropna()

```
Experiments

Try different models

Compare results

Results & Observations
Explain what worked and why.

### 🧠 Golden Rule

A notebook should make sense even after 6 months.

### 🔹 4. Lab: Build Reusable Notebook Template (1 hour)
### 🎯 Goal

Create one notebook that you reuse for:

Every dataset

Every ML experiment

### 📄 Template Sections (Example)
Header
# Project Name
Author: Shilpa Dadhich
Date:
Objective:

Environment Setup
```python
import numpy as np
import pandas as pd

```
Parameters
```python
SEED = 42
EPOCHS = 100

```
Utility Functions
```python
def evaluate_model(model, X, y):
    return model.score(X, y)

```
Experiments

Try multiple models here.

Conclusion
Best model:
Accuracy:
Next steps:

### 🧠 Why this is powerful?

Saves time

Improves consistency

Makes you look professional (important for internships & research)

### 🧪 Practice Questions + Solutions
❓ Q1: What happens if you run cells out of order?

✅ Answer:
Variables may be undefined or contain old values, causing incorrect results.

❓ Q2: Difference between %time and %%time?

✅ Answer:

%time → single line

%%time → entire cell

❓ Q3: Why use widgets instead of input()?

✅ Answer:

Widgets allow real-time interaction

No need to rerun cells

Better UX for experimentation

❓ Q4: Why avoid hardcoded values in notebooks?

✅ Answer:

Makes experiments inflexible

Hard to reproduce results

Parameters should be configurable

❓ Q5: One major benefit of reusable notebook templates?

✅ Answer:
Consistency and speed across multiple ML experiments.

### 🔑 Final Takeaway (Very Important)

Mastering Jupyter is not about running cells —
it’s about thinking, experimenting, and documenting like an ML engineer.