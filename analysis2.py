
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
products = pd.read_csv('../data/products.csv')
users = pd.read_csv('../data/users.csv')
orders = pd.read_csv('../data/orders.csv')

# Sample analysis
top_products = orders.groupby('product_id').sum().sort_values('quantity', ascending=False).head(10)
top_products.plot(kind='bar', title='Top Selling Products')
plt.tight_layout()
plt.savefig('../images/top_selling_products.png')
