import pandas as pd
# Level 1: Pandas Basics (1–10)

# 1. Create a Pandas Series from a list of 5 numbers.
# 2. Create a Series with custom index labels.
# 3. Create a DataFrame from a dictionary.
# 4. Display the first 5 rows of a DataFrame.
# 5. Find the number of rows and columns in a DataFrame.
# 6. Print all column names.
# 7. Use `info()` to inspect a DataFrame.
# 8. Use `describe()` on numeric columns.
# 9. Select one column as a Series.
# 10. Select multiple columns as a DataFrame.

nums = [10, 20, 30, 40, 50]
series = pd.Series(nums)
print(series)

marks = [85, 90, 78, 92, 88]
labels = ['Shilpa','Jhalak','Utsav','Ankush','Rachit']
series_custom = pd.Series(marks, index=labels)
print(series_custom)

data = {
    "Name": ["Shilpa", "Aman", "Riya"],
    "Age": [21, 22, 20],
    "Score": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
score_column = df['Score']
print(score_column)
selected_columns = df[['Name', 'Score']]
print(selected_columns)
