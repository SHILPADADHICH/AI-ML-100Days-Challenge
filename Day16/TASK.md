# Project to Practice Data Wrangling


### 📊 Example Project: Student Performance Data Cleaning
### 🔹 Project Title

Data Wrangling on Student Performance Dataset

### 🔹 Problem Statement (Realistic)

A coaching institute collected student data from multiple sources (forms, Excel, Google Forms).
The data is messy and cannot be used for analysis or ML.

Your task:

Clean, preprocess, and prepare the data for analysis / ML

### 🔹 Raw Dataset (Messy)

We’ll assume this CSV file: students_raw.csv

Student_ID  Age Marks   City    Gender  Attendance  Enrollment_Date
101 18  85  Delhi   M   90  2023-01-15
102 NaN 78  Mumbai  F   85  15/02/2023
103 19  NaN Delhi   Female  88  2023/03/10
104 200 92  Pune    M   NaN March 20, 2023
105 18  45  delhi   F   70  2023-04-01
105 18  45  delhi   F   70  2023-04-01

### 🚨 Problems:

Missing values

```python
Age = 200 ❌

```
Duplicate row

Inconsistent gender labels

Inconsistent city names

Date format mismatch

Categorical values not encoded