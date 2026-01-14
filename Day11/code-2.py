import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")
df.head()
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(7,4))
sns.countplot(x="species", data=df)
plt.title("Count of Each Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
#Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(x="species", y="sepal_length", data=df)
plt.title("Sepal Length Distribution by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.show()
#violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x="species", y="sepal_length", data=df)
plt.title("Violin Plot of Sepal Length")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.show()
#Pair Plot
sns.pairplot(df, hue="species")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()

#KDE Plot
plt.figure(figsize=(6,4))
sns.kdeplot(df["sepal_length"], fill=True)
plt.title("KDE Plot of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Density")
plt.show()

#Heatmap
plt.figure(figsize=(7,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
