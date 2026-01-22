import pandas as pd
import numpy as np

data = {
    'date': pd.date_range('2024-01-01', periods=30),
    'category': np.random.choice(['Electronics', 'Clothing', 'Books'], 30),
    'sales': np.random.randint(100, 1000, 30),
    'price': np.random.randint(200, 2000, 30)
}

df = pd.DataFrame(data)
df.set_index('date', inplace=True)
df.head()

monthly_sales = df.resample('ME').sum()
print("Monthly Sales Summary:")
print(monthly_sales)

#Normalize prices per category

df['price_norm'] = df.groupby('category')['price'].transform(
    lambda x: x / x.mean()
)
df.head()
category_sales = df.groupby('category')['sales'].sum().reset_index()
print("\nTotal Sales by Category:") 
print(category_sales)

#Create a rolling 7-day average of sales
df['sales_7d_avg'] = df['sales'].rolling(window=7).mean()
print("\nDataFrame with 7-Day Rolling Average of Sales:")
print(df.head(10))

#Convert string column to ordered categorical

category_order = ['Books', 'Clothing', 'Electronics']
df['category'] = pd.Categorical(
    df['category'], categories=category_order, ordered=True
)
print("\nDataFrame with Ordered Categorical 'category':")
print(df.head())

#Reduce memory usage of a DataFrame
df['category'] = df['category'].astype('category')
df['sales'] = df['sales'].astype('int32')
df['price'] = df['price'].astype('int32')
df.info()
print("\nDataFrame after Memory Optimization:")
print(df.head())
