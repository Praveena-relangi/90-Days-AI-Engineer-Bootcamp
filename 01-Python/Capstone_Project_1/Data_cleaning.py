import pandas as pd

# Load Dataset
df = pd.read_csv("SuperStore_Dataset.csv")

# Check Missing Values
print("=" * 10, "MISSING VALUES", "=" * 10)
print(df.isnull().sum())

# Check Duplicate Rows
print("=" * 10, "DUPLICATE ROWS", "=" * 10)
duplicate_count = df.duplicated().sum()
print("Duplicate Rows :", duplicate_count)

# Remove Duplicates
df = df.drop_duplicates()

# Check Shape i.e. for number of rows
print("=" * 10, "NEW SHAPE", "=" * 10)
print(df.shape)

# Check format of Dates
print(df["Order Date"].head())
print(df["Ship Date"].head())
# Convert Order Date and Ship Date from str to datetime
'''df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d/%m/%Y"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%d/%m/%Y"
)'''

# verify data type of Order and Ship dates after changing
print(df.dtypes)

# find missing rows
missing_postal = df[df["Postal Code"].isnull()]

print(missing_postal[
    [
        "City",
        "State",
        "Postal Code"
    ]
])

print(df[df["City"] == "Burlington"][
    ["City", "State", "Postal Code"]
])