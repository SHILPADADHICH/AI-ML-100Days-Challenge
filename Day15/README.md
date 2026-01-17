### 🔹 Day 15: Data Wrangling – Deep Dive
What is Data Wrangling?

```python
Data wrangling = turning raw, messy, unreliable data into clean, usable data.

```
Real datasets usually have:

Missing values ❌

Wrong data types ❌

Outliers ❌

Inconsistent text ❌

Duplicate rows ❌

### 🧠 PART 1: Missing Values (Lecture)
1️⃣ What are Missing Values?

Missing values appear as:

NaN (Not a Number)

None

Empty strings ""

Special values like -1, 999, "Unknown"

Example:
```python
import pandas as pd

data = {
```
"Age": [22, 25, None, 30],
"Salary": [30000, None, 50000, 70000],
"City": ["Delhi", None, "Mumbai", "Pune"]
}

```python
df = pd.DataFrame(data)
```
df

2️⃣ Detect Missing Values
df.isnull()

Count missing values per column:
df.isnull().sum()

Percentage of missing data:
df.isnull().mean() * 100

### 💡 Rule of thumb

<5% → safe to drop or fill

5–30% → careful imputation

30% → consider removing column

3️⃣ Handling Missing Values
A. Drop Missing Values

- ❌ Risky (you lose data)

df.dropna()          # drop rows
df.dropna(axis=1)   # drop columns

Use when:

Dataset is large

Missing rows are very few

B. Fill Missing Values (Imputation)
### 🔹 Mean (for numerical data)
df["Age"].fillna(df["Age"].mean(), inplace=True)

Use when:

Data is symmetric

No extreme outliers

### 🔹 Median (best for salary, income)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

✅ Robust against outliers

### 🔹 Mode (for categorical)
df["City"].fillna(df["City"].mode()[0], inplace=True)

### 🔹 Forward / Backward Fill (time-series)
df.fillna(method="ffill")
df.fillna(method="bfill")

### 🔹 Custom Value
df["City"].fillna("Unknown", inplace=True)

4️⃣ Advanced Imputation (Conceptual)

(You’ll use these later in ML)

KNN Imputer

Regression-based imputation

ML-based imputation

### 🧠 PART 2: Outliers (Lecture)
1️⃣ What are Outliers?

```python
Outliers = values far away from normal data

```
Example:

Salary: 30k, 35k, 40k, 45k, 2,00,000 ❌

Outliers can:

Distort mean

Break ML models

Reduce accuracy

2️⃣ Detect Outliers
A. Using IQR (Most Common)
```python
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]
```
outliers

B. Using Z-Score
```python
from scipy.stats import zscore

df["z_score"] = zscore(df["Salary"])
```
df[df["z_score"].abs() > 3]

3️⃣ Handling Outliers
### 🔹 Remove
```python
df = df[(df["Salary"] >= lower) & (df["Salary"] <= upper)]

```
Use when:

Data error

Extremely rare values

### 🔹 Cap (Winsorization)
```python
df["Salary"] = df["Salary"].clip(lower, upper)

```
Best for:

Financial data

### 🔹 Keep Them

Keep if:

Fraud detection

Rare events matter

### 🧠 PART 3: Type Conversions (Lecture)
1️⃣ Why Data Types Matter?

ML models only understand numbers.

```python
Wrong types = broken pipeline ❌

```
2️⃣ Check Data Types
df.dtypes

3️⃣ Convert Types
### 🔹 String → Integer
```python
df["Age"] = df["Age"].astype(int)

```
### 🔹 String → Float
```python
df["Salary"] = df["Salary"].astype(float)

```
### 🔹 Object → Category
```python
df["City"] = df["City"].astype("category")

```
Memory efficient ✔️

### 🔹 Date Conversion
```python
df["Date"] = pd.to_datetime(df["Date"])

```
### 🔹 Extract Date Features
```python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

```
### 🧠 PART 4: PRACTICE – Handle a Messy Dataset
Messy Dataset Example
```python
data = {
```
"Age": ["22", "25", None, "thirty"],
"Salary": ["30000", "?", "50000", "70000"],
"City": ["delhi", "Delhi", "MUMBAI", None]
}

```python
df = pd.DataFrame(data)

```
Step-by-Step Cleaning
1️⃣ Replace invalid values
df.replace("?", None, inplace=True)

2️⃣ Standardize text
```python
df["City"] = df["City"].str.lower().str.strip()

```
3️⃣ Fix numeric columns
```python
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

```
4️⃣ Handle missing
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["City"].fillna(df["City"].mode()[0], inplace=True)

✅ Final Clean Data
df

### 🧠 PART 5: PROJECT – Complete Data Cleaning Workflow
### 🔹 Real-World Workflow (Industry Style)
1️⃣ Load Data
```python
df = pd.read_csv("dataset.csv")

```
2️⃣ Initial Inspection
df.head()
df.info()
df.describe()

3️⃣ Remove Duplicates
df.drop_duplicates(inplace=True)

4️⃣ Handle Missing Values
df.fillna(df.median(), inplace=True)

5️⃣ Handle Outliers
```python
for col in df.select_dtypes(include="number"):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df[col] = df[col].clip(Q1 - 1.5*IQR, Q3 + 1.5*IQR)

```
6️⃣ Fix Data Types
```python
df["date"] = pd.to_datetime(df["date"])

```
7️⃣ Final Check
df.isnull().sum()
df.dtypes

### 🧠 Key Takeaways (VERY IMPORTANT)

✅ Data cleaning takes 60–70% of ML time
✅ Median > Mean for real-world data
✅ Always inspect before cleaning
✅ Never blindly delete data
```python
✅ Clean data = better model without tuning
```