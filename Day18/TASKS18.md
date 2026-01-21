# 📅 Day 18 Task – Pandas Advanced

**100 Days AI/ML Challenge**

---

## 🎯 Goal of the Day

Master advanced Pandas concepts required for real-world data science workflows, especially **time-series handling, categorical data optimization, performance tuning**, and **feature engineering pipelines**.

---

## 🕒 Time Breakdown (5 Hours Total)

* **Lecture (1h):** Time series, categorical data, performance
* **Coding (2h):** Advanced grouping and transformation
* **Practice (1h):** Datetime operations, categorical encoding
* **Lab (1h):** Build a feature engineering pipeline

---

## 📘 1. Lecture (1 Hour)

### A. Time Series in Pandas

Focus on:

* `pd.to_datetime()`
* DatetimeIndex
* Resampling (`resample()`)
* Shifting & rolling windows

Example:

```python
import pandas as pd

df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'sales': [100, 150, 120]
})

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
```

---

### B. Categorical Data

Focus on:

* `astype('category')`
* `.cat.codes`
* Ordered vs unordered categories

Example:

```python
df['grade'] = df['grade'].astype('category')
```

---

### C. Performance Optimization

Learn:

* Vectorization vs loops
* `apply()` vs built-in methods
* Memory optimization using `category` and `int32`

---

## 💻 2. Coding (2 Hours)

### Advanced Grouping & Transformation

Topics:

* `groupby()` with multiple columns
* `agg()` with multiple functions
* `transform()` vs `apply()`

Example:

```python
df.groupby('department')['salary'].agg(['mean', 'max', 'min'])
```

Transform Example:

```python
df['salary_norm'] = df.groupby('department')['salary'].transform(lambda x: x / x.mean())
```

---

## ✍️ 3. Practice (1 Hour)

### A. Datetime Operations

Practice:

* Extract year, month, day
* Filter by date ranges
* Time differences

Example:

```python
df['year'] = df.index.year
df['month'] = df.index.month
```

---

### B. Categorical Encoding

Practice:

* Label encoding
* One-hot encoding

Example:

```python
pd.get_dummies(df, columns=['city'])
```

---

## 🧪 4. Lab (1 Hour)

### Build a Feature Engineering Pipeline

Dataset: **E-commerce Orders**

Columns:

* `order_id`
* `user_id`
* `order_date`
* `category`
* `price`

### Tasks:

1. Convert `order_date` to datetime
2. Create features:

   * Order year
   * Order month
   * Day of week
3. Encode `category` column
4. Create user-level features:

   * Total orders
   * Average order value
5. Optimize memory usage

---

## 🧠 Practice Questions

### Conceptual

1. Difference between `apply()` and `transform()`?
2. Why is `category` dtype memory efficient?
3. What is resampling in time series?

### Coding

1. Group sales by month and calculate total sales
2. Normalize prices per category
3. Create a rolling 7-day average of sales
4. Convert string column to ordered categorical
5. Reduce memory usage of a DataFrame

---

## ✅ Deliverables

* `task.md` completed
* Python notebook with examples
* Feature engineering pipeline code
* Notes on performance improvements

---

🚀 **End of Day 18 – You’re now handling Pandas like a Data Scientist!**
