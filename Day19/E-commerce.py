import pandas as pd
import numpy as np
# Sample e-commerce orders data



orders = pd.DataFrame({
    'order_id': range(1, 11),
    'user_id': [101,102,101,103,102,101,104,103,102,101],
    'order_date': pd.date_range('2024-01-01', periods=10),
    'category': ['Electronics','Books','Books','Clothing','Electronics',
                 'Clothing','Books','Electronics','Clothing','Books'],
    'price': [1200,300,450,800,1500,900,350,2000,700,500]
})

#Covnverting order date to datetime
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders.set_index('order_date', inplace=True)
print("Initial Orders DataFrame:")
print(orders)

#creating time based features
orders['year'] = orders.index.year
orders['month'] = orders.index.month
orders['day_of_week'] = orders.index.day_name()
print("\nOrders DataFrame with Time-based Features:")
print(orders)

#Encoding categorical variables
orders = pd.get_dummies(orders, columns=['category'], drop_first=True)
print("\nOrders DataFrame with One-Hot Encoded Categories:")
print(orders)

#User level feature: Total spend per user
orders['total_spend_per_user'] = orders.groupby('user_id')['price'].transform('sum')
print("\nOrders DataFrame with Total Spend per User:")
print(orders)
#memory optimization
orders['price'] = orders['price'].astype('int32')
orders['user_id'] = orders['user_id'].astype('int16')
orders.info()
print("\nOrders DataFrame after Memory Optimization:")
print(orders)