import pandas as pd

students = {
"Name":["Ravi","Sita","Ram"],
"Marks":[80,90,70],
"City":["Hyd","Vizag","Delhi"]
}

df=pd.DataFrame(students)

# save the dataframe to csv
df.to_csv("students.csv")
# if we don't need index
df.to_csv("students.csv",index=False)
# read the csv into dataframe
new_df=pd.read_csv("students.csv")
print(new_df)