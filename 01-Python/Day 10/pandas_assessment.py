import pandas as pd

students = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 90, 70, 95],
    "City": ["Hyd", "Vizag", "Hyd", "Delhi"]
}

df = pd.DataFrame(students)
print(df[df["Marks"] > 70])
print(df[df["City"] == "Hyd"])
print(df[(df["City"] == "Hyd") & (df["Marks"] > 60)])