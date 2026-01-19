import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 60, 65, 75, 85, 95],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

df.to_csv("./Data/students_cleaned.csv", index=False)
sns.histplot(df["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()


sns.scatterplot(x=df["Study_Hours"], y=df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
