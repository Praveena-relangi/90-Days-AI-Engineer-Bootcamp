import pandas as pd

students = {
    "Name": ["Ravi", "Sita", "Ram", "Geetha", "Kiran"],
    "Marks": [80, 95, 65, 88, 72],
    "City": ["Hyd", "Vizag", "Hyd", "Delhi", "Hyd"]
}

df = pd.DataFrame(students)

print(df)

print(df["Marks"] > 80)

print(df[df["Marks"] > 80])

print(df[df["City"] == "Hyd"])

print(df[(df["City"] == "Hyd") & (df["Marks"] > 70)])

print(df[(df["City"] == "Hyd") | (df["Marks"] > 90)])

print(df.loc[df["Marks"] > 80, ["Name", "Marks"]])

print(df.sort_values("Marks"))