import pandas as pd

employees = {
    "ID":[101,102,103,104,105,106,107,108],
    "Name":["Alice","Bob","Charlie","David","Eva","Frank","Grace","Helen"],
    "Department":["IT","HR","IT","Sales","Finance","HR","IT","Sales"],
    "Salary":[70000,50000,85000,45000,90000,55000,80000,60000],
    "Experience":[3,2,5,1,6,3,4,2]
}

df = pd.DataFrame(employees)

print(df)

#Task 1 : Display only IT employees.
print(df[df["Department"] == "IT"])

#Task 2 : Display employees earning more than $60,000.
print(df[(df["Salary"]>66000)])

#Task 3 : Find the highest-paid employee.
print(df.sort_values("Salary", ascending = False).head(1))

#Task 4 : Find the average salary department-wise.
print(df.groupby("Department")["Salary"].mean())

#Task 5 : Find the number of employees in each department.
print(df.groupby("Department")["Salary"].count())

#Task 6 : Display employees having more than 3 years of experience.
print(df[df["Experience"] > 3])

#Task 7: Display only Name, Salary columns
print(df[["Name", "Salary"]])

#Task 8 : Find the Top 3 highest-paid employees.
print(df.sort_values("Salary", ascending = False).head(3))

#Final Challenge : "Show me the Top 2 IT employees having salary greater than $75,000, sorted by salary."
print("----------------CHALLENGE ACCEPTED---------------------")
print(df[
    (df["Department"] == "IT") & 
    (df["Salary"] > 75000)].sort_values("Salary",
                                         ascending = False
                                         ).head(2))