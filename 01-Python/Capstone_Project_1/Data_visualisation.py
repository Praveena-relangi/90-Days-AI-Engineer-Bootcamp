import matplotlib.pyplot as plt
import pandas as pd

# Load Dataset
df = pd.read_csv("SuperStore_Dataset.csv")

# Sales by Category
category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("Images/sales_by_category.png")
plt.show()

# Sales by Region
region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
plt.bar(region_sales.index, region_sales.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("Images/sales_by_region.png")
plt.show()

# Sales by Customer Segment
segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
plt.bar(segment_sales.index, segment_sales.values)
plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("Images/sales_by_segment.png")
plt.show()

# Top 10 States
top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
plt.bar(top_states.index, top_states.values)
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/top_10_states.png")
plt.show()

# Top 10 cities
top_cities = (
    df.groupby("City")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
plt.bar(top_cities.index, top_cities.values)
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/top_10_cities.png")
plt.show()

# Top 10 products
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(14,6))
plt.bar(top_products.index, top_products.values)
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Images/top_10_products.png")
plt.show()