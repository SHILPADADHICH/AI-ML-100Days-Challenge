### 📊 Day 17: Statistical Visualization (Beginner → Confident)

Goal of Day 17:
Learn how to understand data using graphs, find patterns, detect problems, and prepare data for ML.

### 🔹 What is Statistical Visualization? (Very Basic)

Imagine you have this data:

Marks of students:
45, 50, 52, 55, 60, 90

If I ask:

Are most students scoring high or low?

Is there any unusual value?

Looking at numbers is hard 😵
But draw a graph → answer becomes obvious.

```python
### 👉 Statistical Visualization = Using charts/plots to understand data behavior

```
### 🧠 Why is this important in AI / ML?

Before training ANY ML model, you must:

Understand data distribution

Detect outliers

Find relationships between variables

Check data imbalance

```python
### 📌 ML without visualization = Blind ML

```
### 🟢 LECTURE (1.5h)
1️⃣ Types of Statistical Plots (From Scratch)

We’ll use Python + Matplotlib + Seaborn
(You don’t need math knowledge for now)

### 📌 1. Histogram (MOST IMPORTANT)
❓ What it shows

Distribution of data

Frequency of values

### 🧠 Real-life example

Heights of students:

Are most students tall?

Short?

Average?

### 🔢 Example
```python
import matplotlib.pyplot as plt
import seaborn as sns

data = [150, 152, 155, 160, 162, 165, 170, 180]

```
plt.hist(data)
plt.show()

### 📊 How to read it

X-axis: Value range (height)

Y-axis: Count (how many students)

### 👉 Used to answer:

Is data normal / skewed?

Is data balanced?

### 📌 2. Box Plot (Outlier Detector)
❓ What it shows

Median

Spread of data

Outliers

### 🧠 Example
sns.boxplot(data=data)
plt.show()

### 📦 Box plot parts

Middle line → Median

Box → 25% to 75% data

Dots outside → Outliers

### 📌 Outliers can destroy ML models

### 📌 3. Scatter Plot (Relationship Finder)
❓ What it shows

Relationship between two numerical variables

### 🧠 Example

Study hours vs marks

```python
hours = [1,2,3,4,5,6]
marks = [30,40,50,65,70,85]

```
plt.scatter(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

### 📊 How to read

Upward trend → positive relation

Downward trend → negative relation

### 📌 Very useful before Regression models

### 📌 4. Bar Chart (Category Comparison)
❓ What it shows

Comparison between categories

### 🧠 Example
```python
cities = ['Delhi', 'Mumbai', 'Jaipur']
population = [30, 20, 10]

```
plt.bar(cities, population)
plt.show()

### 📌 Used for:

Gender count

Product categories

Class distribution

### 📌 5. Line Plot (Trend over time)
### 🧠 Example
```python
days = [1,2,3,4,5]
sales = [100, 120, 90, 150, 180]

```
plt.plot(days, sales)
plt.show()

### 📌 Used for:

Time series data

Growth/decline analysis

### 🟢 CODING (2h)
Create Statistical Analysis Visualizations
### 🔹 Dataset (Simple)
```python
import pandas as pd

data = {
```
"Age": [18,19,20,21,22,23,24,25],
"Marks": [50,55,60,65,70,80,85,90],
"Gender": ["M","F","F","M","F","M","F","M"]
}

```python
df = pd.DataFrame(data)

```
1️⃣ Histogram
sns.histplot(df["Marks"], bins=5)
plt.show()

2️⃣ Box Plot
sns.boxplot(x=df["Marks"])
plt.show()

3️⃣ Scatter Plot
sns.scatterplot(x=df["Age"], y=df["Marks"])
plt.show()

4️⃣ Bar Chart
sns.countplot(x=df["Gender"])
plt.show()

### 🟢 PRACTICE (1.5h)
EDA on 2 New Datasets (Beginner-Friendly)
### 📂 Dataset 1: Student Performance
Columns:

Study Hours

Marks

Attendance

Questions to answer:

Are marks normally distributed?

Does study hour affect marks?

Are there outliers?

Visuals to create:

Histogram → Marks

Scatter → Hours vs Marks

Boxplot → Marks

### 📂 Dataset 2: House Prices
Columns:

Area (sq ft)

Price

Location

Questions:

Which location has highest prices?

Any unusual prices?

Relation between area & price?

Visuals:

Boxplot → Price

Scatter → Area vs Price

Bar chart → Location vs Avg Price

### 🧠 Beginner EDA Checklist (SAVE THIS)

Before ML:

- ✔ Histogram → Distribution

- ✔ Boxplot → Outliers

- ✔ Scatter → Relationships

- ✔ Bar chart → Categories

- ✔ Missing values check

### 🚀 What You Should Feel After Day 17

✅ You can look at data and understand it visually
✅ You know which plot to use & why
✅ You are ML-ready (real foundation)