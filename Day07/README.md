### 🐼 Pandas – Part 1 (Day 7)
Why Pandas?

NumPy is great for numbers, but real-world data is:

messy

tabular (rows & columns)

missing values

CSV / Excel / JSON

### 👉 Pandas is built on NumPy and designed for data analysis & cleaning.

### 🔹 PART 1: Core Concepts (Lecture – 1.5h)
1️⃣ Series (1D Data)

A Series is like:

a column in Excel

a labeled NumPy array

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

```
Output:

## 0    10
## 1    20
## 2    30
## 3    40

With custom index
```python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

```
### 📌 Key things to know:

values → s.values

index → s.index

datatype → s.dtype

2️⃣ DataFrame (MOST IMPORTANT 🔥)

A DataFrame is:

2D table (rows + columns)

like Excel / SQL table

```python
data = {
```
"Name": ["Shilpa", "Aman", "Riya"],
"Age": [21, 22, 20],
"Score": [85, 90, 88]
}

```python
df = pd.DataFrame(data)
print(df)

```
### 📌 Think of:

Rows → observations

Columns → features

3️⃣ DataFrame Basics You MUST Know
df.head()      # first 5 rows
df.tail()      # last 5 rows
df.shape       # (rows, columns)
df.columns     # column names
df.info()      # data types & nulls
df.describe()  # statistics (numeric)

### 👉 info() and describe() are used DAILY in ML

4️⃣ Selecting Data
Column selection
df["Age"]          # Series
df[["Age","Score"]]  # DataFrame

Row selection
df.loc[0]     # by label
df.iloc[0]    # by index position

Specific rows & columns
df.loc[0, "Age"]
df.iloc[0, 1]

5️⃣ Filtering (VERY IMPORTANT)
df[df["Age"] > 21]
df[df["Score"] >= 88]

Multiple conditions:

df[(df["Age"] > 20) & (df["Score"] > 85)]

### 🔹 PART 2: Basic Operations (Still Lecture)
Add a new column
```python
df["Passed"] = df["Score"] >= 85

```
Modify column
```python
df["Age"] = df["Age"] + 1

```
Delete column
df.drop("Passed", axis=1, inplace=True)

Handling Missing Values (Intro)
df.isnull()
df.isnull().sum()

Fill missing values:

df.fillna(0)

Drop missing values:

df.dropna()

### 🔹 PART 3: CSV Files (Practice – 1h)
Load CSV
```python
df = pd.read_csv("data.csv")

```
Explore dataset
df.head()
df.info()
df.describe()
df.columns

Common real-world tasks
df["column"].unique()
df["column"].value_counts()
