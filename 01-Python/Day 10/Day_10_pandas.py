import pandas as pd 

# series with default index
marks = pd.Series([10,20,30])
print(marks)

# series with custom index
marks = pd.Series(
[80,90],
index=["Ravi","Sita"]
)
print(marks["Ravi"])

# Data frame
students={
"Name":["A","B"],
"Marks":[50,60]
}
df=pd.DataFrame(students)
print(df.shape)
print(df["Marks"])
print(df[["Name","Marks"]])

# head()
print(df.head()) 

# head with custom value
print(df.head(2))

# tail
print(df.tail())

# tail with custom value
print(df.tail(2))

# info
print(df.info())

# describe
print(df.describe())

# length
print(len(df))

# shape
print(df.shape)

# till now accessed columns
# now accessing rows
students = {
"Name":["A","B","C"],
"Marks":[50,60,70]
}
df=pd.DataFrame(students)

# works with position number
print(df.iloc[1])

# works with index 
print(df.loc[1])

# multile row selection. here 0 is start index 2 is number of elements
print(df.iloc[0:2])
