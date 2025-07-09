import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
products = pd.read_csv('../data/products.csv')
users = pd.read_csv('../data/users.csv')
orders = pd.read_csv('../data/orders.csv')
reviews = pd.read_csv('../data/reviews.csv')

# Merge datasets
data = orders.merge(products, on='product_id').merge(users, on='user_id')

# Top-selling products
top_products = data.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top Selling Products')
plt.xlabel('Quantity Sold')
plt.tight_layout()
plt.savefig('../visuals/top_selling_products.png')

# Peak hours
data['order_time'] = pd.to_datetime(data['order_time'])
data['hour'] = data['order_time'].dt.hour
hourly_orders = data.groupby('hour').size()
plt.figure(figsize=(10,5))
sns.lineplot(x=hourly_orders.index, y=hourly_orders.values)
plt.title('Orders by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('../visuals/orders_by_hour.png')

# User retention
retention = data.groupby('user_id')['order_id'].nunique()
plt.figure(figsize=(8,5))
sns.histplot(retention, bins=30)
plt.title('User Retention (Number of Orders per User)')
plt.xlabel('Number of Orders')
plt.ylabel('Number of Users')
plt.tight_layout()
plt.savefig('../visuals/user_retention.png')
