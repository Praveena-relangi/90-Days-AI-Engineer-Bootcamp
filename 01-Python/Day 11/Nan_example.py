import numpy as np
import pandas as pd

students={
"Name":["Ravi","Sita","Ram"],
"Age":[24,np.nan,25],
"Marks":[80,90,np.nan]
}

df=pd.DataFrame(students)
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.dropna())
print(df.fillna(0))
print(df["Age"].fillna(df["Age"].mean()))