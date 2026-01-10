# Day 09 | Advanced Pandas Mastery 🔍
## 100 Days of AI/ML Challenge

Day 9 focuses on **advanced Pandas features** and **feature engineering introduction**. This builds directly on theoretical understanding from Days 1-8 to create **production-ready data manipulation skills**.

***

## 🎯 Day 09 Objectives

By the end of Day 9, I should be able to:
- Master MultiIndex DataFrames and pivot tables for complex data analysis
- Perform efficient string and DateTime operations on real datasets
- Use `apply`/`map`/`applymap` for custom transformations
- Create reusable data cleaning pipelines
- Understand feature engineering basics for ML preparation

***

## ⏰ Time Breakdown (6.5h)

- **Lectures**: 90 min
- **Coding**: 150 min  
- **Advanced exercises**: 120 min
- **Reflection**: 30 min

***

### Lecture: Advanced Pandas Features
```
MultiIndex DataFrames     → Hierarchical indexing
Pivot tables              → Cross-tabulation
String operations         → Text processing
DateTime operations       → Time series prep
Custom functions (apply/map) → Feature engineering
Kaggle Pandas (final lessons)
```

**Resources:**
- Kaggle Pandas Course (Lessons 8-10): 50 min
- Real Python - Advanced Pandas: 20 min

### Theory Review
```
MultiIndex: df.set_index(['A','B']) → df.loc[('A','North')]
Pivot: df.pivot_table(values='sales', index='product', columns='region')
Apply vs Map: Series.apply(func) vs Series.map(dict)
```

***

## 💻 Hands-On Coding

**Notebook**: `day_9_pandas_mastery.ipynb`

### Exercise 1: MultiIndex & Pivot Tables
```python
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': np.random.choice(['A', 'B', 'C'], 20),
    'Region': np.random.choice(['North', 'South'], 20),
    'Sales': np.random.randint(100, 1000, 20)
}
df = pd.DataFrame(data)

# MultiIndex
multi_idx = df.set_index(['Product', 'Region'])
multi_idx.loc[('A', 'North')]

# Pivot table
pivot = df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')
stacked = pivot.stack()
```

### Exercise 2: String Operations
```python
# String methods chain
df['Product'] = df['Product'].str.upper().str.replace('A', 'Product_A')

# Extract patterns
df['Code'] = df['Product'].str.extract(r'(\w+)')

# Filter with contains
high_sales_a = df[df['Product'].str.contains('A', case=False)]
```

### Exercise 3: DateTime Operations 
```python
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Weekend'] = df['Date'].dt.dayofweek.isin([5,6])

# Resample & rolling
daily_sales = df.set_index('Date')['Sales'].resample('D').sum()
df['MA_3'] = df['Sales'].rolling(3).mean()
```

**Break + Lunch (60 min · 12:30–13:30)**

***

## 🚀 Advanced Exercises

### Exercise 1: Custom Functions with Apply/Map (60 min)
```python
def sales_category(x):
    if x > 800: return 'Excellent'
    elif x > 500: return 'Good'
    else: return 'Fair'

df['Sales_Grade'] = df['Sales'].apply(sales_category)
df['Region_ID'] = df['Region'].map({'North': 1, 'South': 2})

# DataFrame apply
df[['Sales', 'Region_ID']].apply(lambda col: col.mean())
```

### Exercise 2: Production Data Manipulation (60 min)
```python
# Duplicates
df_clean = df.drop_duplicates(subset=['Product', 'Region'], keep='last')

# Transform (group statistics)
df['Product_Avg'] = df.groupby('Product')['Sales'].transform('mean')

# Explode nested lists
df_nested = pd.DataFrame({'A': [[1,2], [3,4]]})
df_nested.explode('A')

# Fill strategies
df['Filled_Sales'] = df['Sales'].fillna(method='ffill')
```

***

## 📝 Documentation

- Create: `day_9_advanced_summary.md`
- GitHub commit: **"Day 9: Pandas Mastery - MultiIndex, Pivot, String/DateTime"**

***

## 🧪 Daily Checklist

- [ ] MultiIndex DataFrames created and queried
- [ ] Pivot tables with stack/unstack working
- [ ] String operations (extract, contains, replace) mastered
- [ ] DateTime components extracted and resampled
- [ ] `apply`/`map` custom functions implemented
- [ ] Advanced manipulation (explode, transform, fillna) practiced
- [ ] GitHub committed ✅

***

## 🧠 Key Learnings & Integration

```
Week 1 Theory (Day 8) → Day 9 Practice
Python functions      → Pandas apply()
Control flow          → String/Date conditions
NumPy arrays          → MultiIndex operations
Data cleaning         → Production pipeline
```

**Feature Engineering Insight**: Every `apply()` is creating a new feature for ML!

***

## 📈 Success Metrics

```
MultiIndex Confidence:     4.5/5
Pivot Tables:              4.7/5  
String/DateTime:           4.3/5
Apply/Map Mastery:         4.6/5
Overall Day Score:         4.5/5 ✅
```

***

**Day 09 Completed ✅**  
**Pandas now production-ready!** → Ready for multi-format data loading (Day 10)

**Tomorrow**: Excel, JSON, SQL data loading + complete pipelines 🚀

**Note**: Advanced Pandas skills unlocked. Feature engineering foundation established! 💪