# 🎯 Most Asked Python & Pandas Interview Questions  
*(For Data Analyst / Data Science Freshers)*

---

## 🐍 Python Interview Questions

### 1. What is the difference between a list and a tuple?
- **List:** Mutable, slower, uses more memory
- **Tuple:** Immutable, faster, memory efficient
- Tuples are often used for fixed data

---

### 2. What is the difference between `==` and `is`?
- `==` checks **value equality**
- `is` checks **memory reference (identity)**

---

### 3. What are mutable and immutable data types?
- **Mutable:** list, dict, set
- **Immutable:** int, float, string, tuple

---

### 4. What is a lambda function?
- Anonymous, single-line function
```python
lambda x: x * 2

---
### 5. What is list comprehension?

A compact way to create lists:

[x**2 for x in range(5) if x % 2 == 0]
---
### 6. What is the difference between append() and extend()?

append() adds one element

extend() adds multiple elements

### 7. What is a dictionary and how is it different from a list?

Dictionary stores key-value pairs

Access is faster using keys

### 8. What is exception handling?

Handling runtime errors using:

try:
...
except:
...
finally:
...

### 9. What are *args and **kwargs?

*args → variable positional arguments

**kwargs → variable keyword arguments

### 10. What is the difference between deep copy and shallow copy?

Shallow copy shares references

Deep copy creates independent objects

### 🐼 Pandas Interview Questions
11. What is Pandas?

Python library for data manipulation and analysis

Built on top of NumPy

12. What is the difference between Series and DataFrame?

Series: 1D labeled array

DataFrame: 2D tabular data structure

13. How do you handle missing values in Pandas?

isnull()

fillna()

dropna()

14. What is the difference between loc and iloc?

loc → label-based indexing

iloc → integer-based indexing

15. What is groupby() used for?

Used to split, apply, and combine data

df.groupby("category").mean()

16. Difference between merge() and concat()?

merge() → SQL-like join

concat() → stack DataFrames

17. What is apply() in Pandas?

Applies a function across rows or columns

18. What is pivot_table()?

Creates spreadsheet-style pivot tables

Used for summarization

19. How do you remove duplicates?
df.drop_duplicates()

20. How do you improve Pandas performance?

Use vectorized operations

Avoid loops

Use categorical dtype

Filter early

### 💡 Interview Tip

Most interviewers don’t expect perfection.
They look for:

Clear fundamentals

Correct terminology

Ability to explain logic

Clarity > Complexity