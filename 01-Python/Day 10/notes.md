# Day 10 Notes - Pandas Basics

## Pandas

Pandas is a Python library used for loading, cleaning, manipulating and analyzing structured/tabular data.

---

## Series

1-D data structure.

Example:

```python
marks = pd.Series([80,90,70])
```

---

## DataFrame

2-D tabular data.

Example:

```python
df = pd.DataFrame(data)
```

---

## Series vs DataFrame

Series

- One dimension
- Single column

DataFrame

- Two dimensions
- Multiple columns

---

## Exploring Data

```python
df.head()
```

First five rows

```python
df.tail()
```

Last five rows

```python
df.info()
```

Dataset summary

```python
df.describe()
```

Statistical summary

```python
df.shape
```

Rows and columns

```python
df.columns
```

Column names

```python
df.dtypes
```

Column data types

---

## Selecting Data

Single column

```python
df["Marks"]
```

Returns Series

Multiple columns

```python
df[["Name","Marks"]]
```

Returns DataFrame

---

## loc vs iloc

loc

- Uses labels

iloc

- Uses position numbers

---

## Filtering

Example

```python
df[df["Marks"] > 80]
```

Multiple conditions

```python
df[(df["Marks"] > 80) & (df["City"] == "Hyd")]
```

Use

& → AND

| → OR

Always use parentheses.

---

## Sorting

```python
df.sort_values("Marks")
```

Descending

```python
df.sort_values("Marks", ascending=False)
```

---

## Adding Columns

```python
df["Grade"] = ["A","B","C"]
```

---

## Updating Columns

```python
df["Marks"] = df["Marks"] + 10
```

---

## Removing Columns

```python
df = df.drop("Marks", axis=1)
```

or

```python
df.drop("Marks", axis=1, inplace=True)
```

---

## Interview Questions

Difference between Series and DataFrame

Series

- Single column

DataFrame

- Multiple columns

---

Difference between loc and iloc

loc

- Label based

iloc

- Position based

---

Difference between head() and tail()

head()

- First rows

tail()

- Last rows

---

Difference between NumPy and Pandas

NumPy

- Numerical arrays

Pandas

- Structured/tabular data

---

## Key Takeaways

✔ Pandas is built on top of NumPy

✔ Filtering uses Boolean masks

✔ Single column → Series

✔ Multiple columns → DataFrame

✔ loc uses labels

✔ iloc uses positions

✔ DataFrames are the most commonly used structure in Data Analysis and Machine Learning