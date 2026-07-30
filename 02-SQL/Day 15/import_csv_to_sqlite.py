import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("SuperStore_Dataset.csv", encoding="latin1")

# Create SQLite database
conn = sqlite3.connect("SuperStore.db")

# Create table and import data
df.to_sql("SuperStore", conn, if_exists="replace", index=False)

conn.close()

print("✅ CSV imported successfully into SuperStore.db")