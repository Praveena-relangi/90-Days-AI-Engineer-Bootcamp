import pandas as pd

employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103],
    "Name": ["Ravi", "Sita", "Ram"]
})

salaries = pd.DataFrame({
    "EmployeeID": [101, 102, 104],
    "Salary": [50000, 45000, 70000]
})

print(pd.merge(employees, salaries, on="EmployeeID"))