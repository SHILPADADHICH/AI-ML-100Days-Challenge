### 🌟 Day 10 – Visualization (AI/ML Challenge)

(Deep Explanation + Solved Practice)

### 🔍 PART 1: LECTURE TASKS (1.5h) — CONCEPTS EXPLAINED
1️⃣ Why Visualization is Important in AI/ML

Visualization is not “just plotting graphs”. In ML, it helps you:

### 📌 Before Training (EDA)

Understand data distribution

Detect outliers

Find correlations

Identify imbalance (very important!)

### 📌 During Training

Track loss vs epochs

Track accuracy vs epochs

Detect overfitting / underfitting

### 📌 After Training

Evaluate model performance

Explain results to non-technical people

Compare multiple models

### 👉 Rule:

If you don’t visualize your data, you don’t understand your data.

2️⃣ Matplotlib Basics (FOUNDATION)
### 🔹 pyplot workflow

Matplotlib works like drawing on paper:

Create figure

Draw plot

Add labels

Show / save

```python
import matplotlib.pyplot as plt

```
plt.plot(x, y)
plt.show()

### 🔹 Figure vs Axes (VERY IMPORTANT)
Term	Meaning
Figure	Whole window
Axes	Actual plot area
```python
fig, ax = plt.subplots()
```
ax.plot(x, y)

### 👉 Think:
```python
Figure = notebook page
Axes = graph drawn on that page

```
### 🔹 Labels, Titles, Legends
plt.title("Accuracy vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

```python
### 💡 Always add these — no labels = bad ML practice

```
### 🔹 Colors, Markers, Linestyles
plt.plot(x, y, color="red", marker="o", linestyle="--")

Element	Purpose
color	differentiate plots
marker	highlight points
linestyle	trend visibility
3️⃣ Seaborn Basics
### 🔹 Seaborn vs Matplotlib
Matplotlib	Seaborn
Low-level	High-level
Manual styling	Automatic styling
Any plot	Statistical plots

### 👉 Use Matplotlib for control
### 👉 Use Seaborn for EDA & statistics

### 🔹 Seaborn Datasets
```python
import seaborn as sns

```
sns.load_dataset("iris")

Popular ones:

iris

tips

penguins

flights

### 🔹 Themes & Styles
sns.set_theme(style="darkgrid")

Styles:

whitegrid

darkgrid

ticks

white

4️⃣ Choosing the Right Plot (VERY EXAM + INTERVIEW IMPORTANT)
Purpose	Plot
Distribution	Histogram, KDE
Comparison	Bar, Box
Relationship	Scatter, Regression
Composition	Pie, Area
Correlation	Heatmap
✍️ Deliverable Notes (You can directly use this)

Histogram → data distribution

Box plot → outliers

Scatter → relationship

Heatmap → correlation

Line plot → trends over time

### 💻 PART 2: CODING TASKS (2.5h)

We’ll use Seaborn datasets.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

```
### 🔵 MATPLOTLIB PLOTS (1–8)
1️⃣ Line Plot

### 📌 Used for trends

```python
x = [1,2,3,4,5]
y = [10,20,25,30,40]

```
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

### 🧠 Shows change over time

2️⃣ Multiple Line Plot

### 📌 Compare models

plt.plot(x, y, label="Model A")
plt.plot(x, [12,18,28,35,45], label="Model B")
plt.legend()
plt.show()

3️⃣ Bar Chart

### 📌 Compare categories

```python
categories = ["A", "B", "C"]
values = [10, 25, 15]

```
plt.bar(categories, values)
plt.show()

4️⃣ Horizontal Bar Chart

### 📌 Long labels

plt.barh(categories, values)
plt.show()

5️⃣ Histogram

### 📌 Data distribution

```python
data = np.random.randn(1000)

```
plt.hist(data, bins=30)
plt.show()

6️⃣ Scatter Plot

### 📌 Relationship between variables

plt.scatter(x, y)
plt.show()

7️⃣ Pie Chart

### 📌 Composition

plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.show()

8️⃣ Area Plot

### 📌 Cumulative trends

plt.fill_between(x, y)
plt.show()

### 🟣 SEABORN PLOTS (9–15)
```python
df = sns.load_dataset("iris")

```
9️⃣ Count Plot

### 📌 Frequency

sns.countplot(x="species", data=df)
plt.show()

### 🔟 Box Plot

### 📌 Outliers detection

sns.boxplot(x="species", y="sepal_length", data=df)
plt.show()

1️⃣1️⃣ Violin Plot

### 📌 Distribution + density

sns.violinplot(x="species", y="sepal_length", data=df)
plt.show()

1️⃣2️⃣ KDE Plot

### 📌 Probability density

sns.kdeplot(df["sepal_length"])
plt.show()

1️⃣3️⃣ Heatmap

### 📌 Correlation

sns.heatmap(df.corr(), annot=True)
plt.show()

1️⃣4️⃣ Pair Plot

### 📌 Complete EDA

sns.pairplot(df, hue="species")

1️⃣5️⃣ Regression Plot

### 📌 Trend + prediction

sns.regplot(x="sepal_length", y="petal_length", data=df)
plt.show()

### 🧪 PART 3: LAB — RESEARCH PLOTS (1h)
1️⃣ Accuracy vs Epoch
```python
epochs = range(1,11)
accuracy = [0.6,0.65,0.7,0.75,0.8,0.82,0.85,0.87,0.88,0.9]

```
plt.plot(epochs, accuracy)
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Epoch")
plt.show()

2️⃣ Confusion Matrix Heatmap
```python
cm = np.array([[50,5],[3,42]])

```
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

3️⃣ Feature Importance Bar Chart
```python
features = ["age", "salary", "experience"]
importance = [0.2, 0.5, 0.3]

```
plt.bar(features, importance)
plt.show()

4️⃣ Loss vs Epoch
```python
loss = [1.2,1.0,0.8,0.6,0.5,0.4,0.35,0.3,0.28,0.25]

```
plt.plot(epochs, loss)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

### 🗂️ PART 4: REVIEW (30 min)
### 📁 Folder Structure
visualization_gallery/
├── matplotlib/
├── seaborn/
├── research_plots/
├── README.md
## Final Concept Review (VERY IMPORTANT)
Best plots for Classification

Confusion matrix

Count plot

ROC curve (later)

Best plots for Regression

Regression plot

Line plot

Residual plot

Best plots for EDA

Pair plot

Histogram

Box plot

Heatmap
