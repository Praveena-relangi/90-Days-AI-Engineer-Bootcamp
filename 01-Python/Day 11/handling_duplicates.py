import pandas as pd

df = pd.DataFrame({
    "ID": [1, 2, 2, 3],
    "Name": ["A", "B", "B", "C"],
    "Marks": [80, 90, 90, 70]
})

# To finf the duplicate row. returns boolean output
print(df.duplicated())

# To find number of duplicate rows
print(df.duplicated().sum())

# To drop duplicate rows
print(df.drop_duplicates())