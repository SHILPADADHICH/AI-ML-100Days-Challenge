import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/computer/AI-ML-100Days-Challenge/Day20/Students Social Media Addiction.csv"


df = pd.read_csv(file_path)  # Load the dataset using KaggleDatasetAdapter
print("Dataset loaded successfully.")

print("First 5 records:", df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Fill missing values with column mean for numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    df[col].fillna(df[col].mean(), inplace=True)
print("Missing values filled with column means for numerical columns.")
print("DataFrame after handling missing values:\n", df.head())



duplicate_values = df.duplicated().sum()
print("Number of duplicate records:", duplicate_values)

data_type = df.dtypes

print("Data types of each column:\n", data_type)

#graphical analysis

#Distribution of a numerical column (e.g., 'Age' if it exists)
if 'Age' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=30, kde=True)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

    #Age and Social Media Addiction Score relationship
if 'Addicted_Score' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Addicted_Score', data=df)
    plt.title('Age vs Social Media Addiction Score')
    plt.xlabel('Age')
    plt.ylabel('Social Media Addiction Score')
    
    plt.show()
    
#Correlation heatmap for numerical features
numerical_features = df.select_dtypes(include=[np.number])
plt.figure(figsize=(12, 8))
correlation_matrix = numerical_features.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap of Numerical Features')
plt.show()
#histogram of Social Media Addiction Score
if 'Addicted_Score' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=30, kde=True)
    plt.title('Distribution of Social Media Addiction Score')
    plt.xlabel('Age')
    plt.ylabel('Addicted_Score')
    plt.show()

print(df.columns)
