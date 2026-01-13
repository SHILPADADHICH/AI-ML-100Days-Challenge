# Day 11 — Seaborn & Statistical Visualization(Part-2)

## Objective

Learn Seaborn from scratch and understand how statistical visualizations help in Exploratory Data Analysis (EDA) for AI/ML.

This day focuses on **understanding patterns in data**, not just drawing graphs.

---

## Time Breakdown

* Learning Concepts: 45 min
* Coding & Practice: 1.5–2 hours
* Review & Notes: 30 min

---

## Part 1: Concepts to Understand (Beginner Friendly)

### 1. What is Seaborn?

* Built on top of Matplotlib
* Cleaner and more beautiful plots
* Best suited for statistical analysis and EDA

### 2. Why Seaborn is Important in ML

* Helps detect class imbalance
* Helps find outliers
* Helps understand feature relationships
* Helps decide feature selection

### 3. Seaborn vs Matplotlib

* Matplotlib → control & custom plots
* Seaborn → quick insights & statistics

---

## Part 2: Dataset

Use a built-in Seaborn dataset:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
```

Dataset info:

* Features: sepal_length, sepal_width, petal_length, petal_width
* Target: species

---

## Part 3: Mandatory Plots (Complete All)

### 1. Count Plot

**Purpose:** Check class distribution

Task:

* Plot count of each species
* Add title

Question:

* Is the dataset balanced?

---

### 2. Box Plot

**Purpose:** Detect outliers

Task:

* Box plot of sepal_length vs species

Question:

* Which species has most variation?

---

### 3. Violin Plot

**Purpose:** Distribution + density

Task:

* Violin plot of sepal_length vs species

Question:

* Which species has wider distribution?

---

### 4. KDE Plot

**Purpose:** Understand data shape

Task:

* KDE plot of sepal_length
* Use fill=True

Question:

* Is the distribution skewed or normal?

---

### 5. Heatmap (Correlation)

**Purpose:** Feature relationships

Task:

* Create correlation heatmap
* Use annot=True

Question:

* Which two features are most correlated?

---

### 6. Pair Plot (Optional but Recommended)

**Purpose:** Complete EDA in one plot

Task:

* Pair plot with hue = species

Question:

* Can classes be separated visually?

---

## Part 4: Practice Questions (Answer in Markdown Cells)

1. Which plot helped you identify class imbalance?
2. Which plot is best for outlier detection?
3. Which features seem important for classification?
4. Why is heatmap important before training a model?

---

## Part 5: Saving & Organization

Save each plot as `.png` file.

Folder structure:

```
visualization_gallery/
└── day10B_seaborn/
```

---

## Review Checklist

* [ ] Dataset loaded successfully
* [ ] 5+ Seaborn plots created
* [ ] Titles added to all plots
* [ ] Practice questions answered
* [ ] Plots saved in folder

---

## Outcome of Day 10B

By the end of this day, you should:

* Understand Seaborn basics
* Know how to analyze data visually
* Identify patterns, outliers, and correlations
* Feel confident moving to research-level plots (Day 12 Part 3)

---


