import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
os.makedirs("plots", exist_ok=True)

df = sns.load_dataset("tips")

sns.histplot(df["total_bill"])
plt.title("Total Bill Distribution")
plt.savfig("plots/hist_plot.png")
plt.show()
plt.close() 

sns.scatterplot(data=df, x="total_bill", y="tip", hue="time")
plt.show()

sns.boxplot(x=df["total_bill"])
plt.show()
sns.barplot(data=df, x="day", y="total_bill", ci=None)
plt.show()
sns.countplot(x="day", data=df)
plt.show()
sns.violinplot(x="day", y="total_bill", data=df)
plt.show()
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()




