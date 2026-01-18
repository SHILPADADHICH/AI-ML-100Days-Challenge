import pandas as pd

data = {
    "Student_ID": [101,102,103,104,105,105],
    "Age": [18,None,19,200,18,18],
    "Marks": [85,78,None,92,45,45],
    "City": ["Delhi","Mumbai","Delhi","Pune","delhi","delhi"],
    "Gender": ["M","F","Female","M","F","F"],
    "Attendance": [90,85,88,None,70,70],
    "Enrollment_Date": [
        "2023-01-15",
        "15/02/2023",
        "2023/03/10",
        "March 20, 2023",
        "2023-04-01",
        "2023-04-01"
    ]
}

df = pd.DataFrame(data)
df.to_csv("students_raw.csv", index=False)
#checking missing values
df.isnull().sum()
df["Age"].fillna(df["Age"].median(), inplace=True)

df.duplicated().sum()
df.drop_duplicates(inplace=True)