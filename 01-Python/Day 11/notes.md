# Day 11 Notes - Advanced Pandas

# Reading CSV

```python
df = pd.read_csv("students.csv")
```

Loads a CSV file into a DataFrame.

---

# Writing CSV

```python
df.to_csv("students.csv", index=False)
```

Writes a DataFrame to a CSV file.

`index=False` prevents Pandas from writing row indexes to the file.

---

# Missing Values (NaN)

NaN means the value is missing or unavailable.

Example:

```python
import numpy as np

df = pd.DataFrame({
    "Marks":[80, np.nan, 70]
})
```

---

# Detect Missing Values

```python
df.isnull()
```

Returns a Boolean DataFrame.

---

# Count Missing Values

```python
df.isnull().sum()
```

Returns the number of missing values in each column.

---

# Remove Missing Values

```python
df.dropna()
```

Removes rows containing missing values.

Returns a new DataFrame.

---

# Fill Missing Values

Replace with zero

```python
df.fillna(0)
```

Replace with mean

```python
df["Marks"].fillna(df["Marks"].mean())
```

Pandas ignores NaN while calculating the mean.

---

# Duplicate Records

Detect duplicates

```python
df.duplicated()
```

Returns True for duplicate rows.

Count duplicates

```python
df.duplicated().sum()
```

---

# Remove Duplicates

```python
df.drop_duplicates()
```

Returns a new DataFrame.

Remove duplicates based on a specific column

```python
df.drop_duplicates(subset="Name")
```

---

# GroupBy

Groups similar rows together before performing calculations.

Example

```python
df.groupby("Department")["Salary"].mean()
```

---

# Common Aggregation Functions

Average

```python
.mean()
```

Maximum

```python
.max()
```

Minimum

```python
.min()
```

Total

```python
.sum()
```

Count

```python
.count()
```

Multiple calculations

```python
.agg(["mean","max","min","sum","count"])
```

---

# count() vs size()

count()

- Counts only non-null values

size()

- Counts all rows

---

# Merge

Combine two DataFrames using a common key.

Example

```python
pd.merge(df1, df2, on="EmployeeID")
```

`on` specifies the common column used for matching rows.

Default merge type is **Inner Join**.

---

# Interview Questions

## What is NaN?

NaN represents missing or unavailable data in a dataset.

---

## Why are missing values a problem?

Many data analysis techniques and Machine Learning algorithms cannot work properly with missing values. They should be removed or replaced before training a model.

---

## What is groupby()?

groupby() groups rows based on one or more columns and allows aggregate operations such as mean(), sum(), count(), max(), and min() to be performed on each group independently.

---

## What is merge()?

merge() combines two or more DataFrames using a common key column.

---

## Difference between count() and size()

count()

- Counts only non-null values

size()

- Counts all rows

---

## Difference between duplicated() and drop_duplicates()

duplicated()

- Identifies duplicate rows

drop_duplicates()

- Removes duplicate rows

---

# Key Takeaways

✔ Real-world datasets contain missing values and duplicate records.

✔ Data cleaning is the first step before analysis or Machine Learning.

✔ groupby() is one of the most important Pandas functions.

✔ merge() is the Pandas equivalent of SQL JOIN.

✔ CSV is the most common format used for storing tabular data.

✔ Clean data leads to better analysis and better Machine Learning models.