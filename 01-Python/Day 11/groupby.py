import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Salary": [50000, 40000, 60000, 45000, 50000]
})

# mean
print(df.groupby("Department")["Salary"].mean())

# max and min
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())

# count
print(df.groupby("Department")["Salary"].count())

# size
print(df.groupby("Department")["Salary"].size())

# sum
print(df.groupby("Department")["Salary"].sum())

# multiple aggregations
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum", "count"]))