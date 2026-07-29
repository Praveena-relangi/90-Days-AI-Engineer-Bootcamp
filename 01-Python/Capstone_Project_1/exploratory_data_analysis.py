import pandas as pd

# Load Dataset
df = pd.read_csv("SuperStore_Dataset.csv")

# Calculate Company total revenue
print("=" * 10, "TOTAL SALES", "=" * 10)
print(df["Sales"].sum())

# Calculate Number of Categories
print("=" * 10, "CATEGORIES", "=" * 10)
print(df["Category"].unique())
print("Total Categories :", df["Category"].nunique())

# Calculate Sales by Category
category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)
print(category_sales)

# Calculate Sales by Region
region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)
print(region_sales)

# Sales by Segment
segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)
print(segment_sales)

# Top 10 states by sales
top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print(top_states)

# Top 10 cities
top_cities = (
    df.groupby("City")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print(top_cities)

# Highest Selling Products
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print(top_products)