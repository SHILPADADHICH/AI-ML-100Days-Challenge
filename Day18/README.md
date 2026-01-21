1️⃣ Time Series in Pandas (Lecture – 1h)
### 🔹 What is Time Series?

Any data indexed or dependent on time (date, timestamp).

Examples:

App daily active users

Food orders per hour

Stock prices

Website traffic per day

### 🔹 Why Pandas is powerful for Time Series

Because once your column is datetime, Pandas lets you:

Filter by date ranges

Aggregate by week/month/year

Create lag features (used heavily in ML)

Apply rolling statistics

### 🔹 Key Operations Explained
✅ Convert to datetime
```python
df['order_date'] = pd.to_datetime(df['order_date'])

```
Without this, Pandas treats dates like strings → no time intelligence.

✅ Set datetime as index (important)
df.set_index('order_date', inplace=True)

Now you can:

Resample

Use .loc['2024-01']

Extract year/month easily

✅ Resampling (VERY IMPORTANT)

Used when you want to change frequency.

Example:

Daily sales → Monthly sales

df.resample('M')['sales'].sum()

Common frequencies:

D → Day

W → Week

M → Month

Y → Year

✅ Rolling Window (used in ML features)
```python
df['7_day_avg'] = df['sales'].rolling(7).mean()

```
Used in:

Trend detection

Smoothing noisy data

Feature engineering

2️⃣ Categorical Data (Lecture – 1h)
### 🔹 What is Categorical Data?

Data with limited repeated values:

City

Gender

Product category

Department

### 🔹 Why category dtype matters

Benefits:

### 🚀 Faster operations

### 💾 Less memory

### 📊 Better groupby performance

```python
df['city'] = df['city'].astype('category')

```
### 🔹 Ordered vs Unordered Categories

Example:

```python
grades = ['low', 'medium', 'high']
df['priority'] = pd.Categorical(
```
df['priority'],
categories=grades,
ordered=True
)

Now Pandas understands:

high > medium > low

This is VERY useful in ML preprocessing.

### 🔹 Encoding Categories
Label Encoding
```python
df['category_code'] = df['category'].cat.codes

```
One-Hot Encoding
pd.get_dummies(df, columns=['category'])

Used when feeding data into ML models.

3️⃣ Performance Optimization (Lecture – 1h)
### 🔹 Why performance matters

Real datasets:

Lakhs / millions of rows

```python
Loops = ❌ slow

Vectorization = ✅ fast

```
- ❌ Bad (loop)
```python
for i in range(len(df)):
    df['new'][i] = df['a'][i] * 2

```
✅ Good (vectorized)
```python
df['new'] = df['a'] * 2

```
### 🔹 apply() vs Built-ins

apply() → flexible but slower

Built-in functions → faster

Rule:

Use apply only if no built-in exists

4️⃣ Advanced Grouping & Transformation (Coding – 2h)
### 🔹 groupby() + agg()
df.groupby('department')['salary'].agg(['mean', 'max'])

Used in:

Business reports

Analytics dashboards

### 🔹 transform() vs apply() (VERY IMPORTANT)
transform → returns same shape
```python
df['salary_norm'] = df.groupby('dept')['salary'].transform(
```
lambda x: x / x.mean()
)

apply → can change shape
df.groupby('dept').apply(custom_function)

### 👉 Use transform for feature creation.

5️⃣ Datetime Practice (Practice – 1h)
### 🔹 Feature extraction from dates
```python
df['year'] = df.index.year
df['month'] = df.index.month
df['dayofweek'] = df.index.dayofweek

```
These become ML features.

### 🔹 Date filtering
df.loc['2024-01-01':'2024-01-31']

Used in:

Monthly reports

Experiment analysis

6️⃣ Feature Engineering Pipeline (Lab – 1h)
### 🔹 What is Feature Engineering?

Converting raw data → ML-ready numerical features.

### 🔹 Example Pipeline Logic (Real World)

For an E-commerce / Food App:

Date → year, month, weekday

Category → encoded

User → total orders, avg order value

Prices → normalized

### 🔹 Why this matters

This is:

Asked in interviews

Used in real ML projects

Core of Data Scientist role

### 🧠 How Day 18 Helps You

By finishing this day, you can:

Handle real datasets confidently

Build ML-ready tables

Optimize Pandas like professionals

Talk about feature engineering in interviews
