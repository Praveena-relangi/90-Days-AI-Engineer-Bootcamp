import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C","D"],
    "Department":["IT","HR","IT","Sales"],
    "Salary":[60000,45000,75000,50000]
})

# Filtering data
after_filtering = df[df["Department"] == "IT"]
print(after_filtering)

# Multiple conditions
multi_cond = df[
    (df["Department"]=="IT") &
    (df["Salary"]>50000)
]
print(multi_cond)

# OR condition
or_cond = df[
    (df["Department"]=="IT") |
    (df["Department"]=="HR")
]
print(or_cond)

# ascending 
ascend = df.sort_values("Salary")
print(ascend)

# descnding
descend = df.sort_values("Salary", ascending=False)
print(descend)

# Top N rows
top_n_rows = df.sort_values(
    "Salary",
    ascending=False
).head(3)
print(top_n_rows)

# selecting specific column
specific_col = df[["Name","Salary"]]
print(specific_col)

# combo
combo = df[
    df["Department"]=="IT"
].sort_values(
    "Salary",
    ascending=False
).head(2)
print(combo)