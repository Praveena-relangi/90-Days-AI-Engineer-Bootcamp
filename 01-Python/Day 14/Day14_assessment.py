import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C","D","E"],
    "Department":["IT","HR","IT","Sales","HR"],
    "Salary":[60000,45000,75000,50000,55000]
})

# Filtering data for HR
hr_filtering = df[df["Department"] == "HR"]
print(hr_filtering)

# salary filter
salary_filter = df[(df["Salary"]>55000)]
print(salary_filter)

# salary in descending order
sal_descend = df.sort_values("Salary", ascending=False)
print(sal_descend)

# top 2 high paid employees
top_2_rows = df.sort_values(
    "Salary",
    ascending=False
).head(2)
print(top_2_rows)

# Q5 answer for now i learned filtering using pandas. So I will reply with Filtering