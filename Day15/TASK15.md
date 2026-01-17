# 📅 Day 15 – Data Wrangling Deep Dive

## 🎯 Goal
Understand and implement complete data wrangling workflows used in real-world AI/ML projects, focusing on handling missing values, outliers, and data type inconsistencies.

---

## 🧠 Topics Covered

### 1. Missing Values
- Identifying missing values (`NaN`, `None`, empty strings)
- Understanding impact on analysis and models
- Techniques:
  - Dropping rows/columns
  - Mean, median, mode imputation
  - Forward fill / backward fill
  - Custom value replacement

---

### 2. Outliers
- What are outliers and why they matter
- Detection methods:
  - IQR (Interquartile Range)
  - Z-score
- Handling strategies:
  - Removal
  - Capping (Winsorization)
  - Retaining for special use-cases

---

### 3. Data Type Conversion
- Importance of correct data types
- Common conversions:
  - Object → Numeric
  - String → Datetime
  - Object → Category
- Feature extraction from datetime columns

---

## 🛠️ Practice Tasks

### Task 1: Missing Value Handling
- Load a dataset with missing values
- Identify:
  - Total missing values
  - Missing percentage per column
- Apply:
  - Median imputation for numerical columns
  - Mode imputation for categorical columns

---

### Task 2: Outlier Detection & Treatment
- Select numerical columns
- Detect outliers using IQR method
- Apply capping instead of deletion
- Compare statistics before vs after treatment

---

### Task 3: Fix Data Types
- Convert:
  - Invalid numeric strings to numbers
  - Date columns to datetime format
- Extract:
  - Year, month from datetime column

---

## 🚀 Mini Project: Complete Data Cleaning Workflow

### Objective
Transform a messy dataset into a clean, model-ready dataset.

### Steps
1. Load dataset
2. Initial inspection (`info`, `describe`)
3. Remove duplicates
4. Handle missing values
5. Detect and treat outliers
6. Fix data types
7. Perform final validation checks

---

## ✅ Deliverables
- Cleaned dataset
- Jupyter Notebook with:
  - Clear section headers
  - Step-by-step explanations
  - Clean, readable code

---

## 🧠 Key Learnings
- Data quality directly impacts model performance
- Median is often more robust than mean
- Outliers require context-aware handling
- Data wrangling is iterative, not linear

---

## ⏱️ Time Allocation
- Lecture / Reading: 1.5 hours  
- Hands-on Practice: 3 hours  
- Mini Project: 1.5 hours  

---

## 📌 Notes
Focus on **why** each cleaning step is required, not just **how** to do it.  
Think from the perspective of making data usable for machine learning models.

---
