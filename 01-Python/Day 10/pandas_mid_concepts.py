import pandas as pd

students = {
    "Name":["A","B","C"],
    "Marks":[80,90,70]
}

df = pd.DataFrame(students)
print(df)

#Add new column
df["Grade"] = ["B","A","C"]
print(df)

#Add new calculated column
df["FinalMarks"] = df["Marks"] + 5
print(df)

#drop() won't modify the dataframe by default
print(df.drop("Grade", axis=1))

# drop() modifies the dataframe if we assign it to same dataframe.
# can also be written as df.drop("Grade", axis=1, inplace=True)
df = df.drop("Grade", axis=1)
print(df)