# 📅 Day 19 – Pandas Advanced  (part-2)
**100 Days AI/ML Challenge**

---

## 🎯 Goal of the Day

Master advanced Pandas concepts required for real-world data science workflows, including:

- Time series handling
- Categorical data optimization
- Performance tuning
- Feature engineering pipelines

---

## 🕒 Time Breakdown (5 Hours)

- **Lecture (1h):** Time series, categorical data, performance optimization  
- **Coding (2h):** Advanced grouping and transformation  
- **Practice (1h):** Datetime operations, categorical encoding  
- **Lab (1h):** Feature engineering pipeline  

---

## 📘 1. Lecture Tasks (1 Hour)

### A. Time Series in Pandas

Learn and practice:

- `pd.to_datetime()`
- `DatetimeIndex`
- Resampling using `resample()`
- Shifting and rolling windows

**Practice Example:**
```python
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

B. Categorical Data

Understand:

astype('category')

.cat.codes

Ordered vs unordered categories

Practice Example:

```python
df['grade'] = df['grade'].astype('category')

```
C. Performance Optimization

Focus on:

Vectorization vs loops

apply() vs built-in Pandas methods

Memory optimization using:

category

int32, float32

### 💻 2. Coding Tasks (2 Hours)
Advanced Grouping & Transformation

Practice:

groupby() with multiple columns

agg() with multiple functions

transform() vs apply()

Examples:

df.groupby('department')['salary'].agg(['mean', 'max', 'min'])

```python
df['salary_norm'] = df.groupby('department')['salary'].transform(
```
lambda x: x / x.mean()
)

✍️ 3. Practice Tasks (1 Hour)
A. Datetime Operations

Extract year, month, day

Filter rows by date range

Calculate time differences

Example:

```python
df['year'] = df.index.year
df['month'] = df.index.month

```
B. Categorical Encoding

Practice:

Label encoding using .cat.codes

One-hot encoding using pd.get_dummies()

Example:

pd.get_dummies(df, columns=['city'])

### 🧪 4. Lab Task (1 Hour)
Feature Engineering Pipeline – E-commerce Orders

Dataset Columns:

order_id

user_id

order_date

category

price

Tasks:

Convert order_date to datetime

Create time-based features:

Order year

Order month

Day of week

Encode the category column

Create user-level features:

Total orders per user

Average order value per user

Optimize memory usage of the DataFrame

### 🧠 Interview Questions
Conceptual Questions

What is the difference between apply() and transform() in Pandas?

Why is category dtype more memory efficient than object?

What is resampling in time series data?

When would you prefer rolling() over groupby()?

Why is vectorization faster than loops in Pandas?

What happens if transform() returns a different shape?

Explain ordered vs unordered categorical data.

Coding / Practical Questions

Group sales data by month and calculate total sales.

Normalize prices within each category.

Create a rolling 7-day average of sales.

Convert a string column into an ordered categorical column.

Reduce memory usage of a large DataFrame.

Extract day name from a datetime column.

Encode a categorical column using both label encoding and one-hot encoding.

