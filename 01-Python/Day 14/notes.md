# 📝 Bootcamp Week 2 – Day 14 Notes

# Data Manipulation using Pandas

---

## Filtering

Select rows satisfying conditions.

```python
df[df["Department"] == "HR"]
```

---

## Multiple Conditions

AND

```python
(df["Department"] == "IT") & (df["Salary"] > 50000)
```

OR

```python
(df["Department"] == "IT") | (df["Department"] == "HR")
```

---

## Sorting

Ascending

```python
df.sort_values("Salary")
```

Descending

```python
df.sort_values("Salary", ascending=False)
```

---

## Top Records

Top 5

```python
df.head()
```

Top 3 highest salaries

```python
df.sort_values("Salary", ascending=False).head(3)
```

---

## GroupBy

Average salary

```python
df.groupby("Department")["Salary"].mean()
```

Count employees

```python
df.groupby("Department")["Salary"].count()
```

---

## Selecting Columns

```python
df[["Name", "Salary"]]
```

---

## Experience Filter

```python
df[df["Experience"] > 3]
```

---

# Interview Questions

### Which Pandas operation is used to retrieve rows based on conditions?

Answer:

Filtering

---

### Difference between AND and OR?

AND

Both conditions should be True.

OR

At least one condition should be True.

---

### How to sort in descending order?

```python
df.sort_values("Salary", ascending=False)
```

---

### How to find Top N records?

```python
df.sort_values("Salary", ascending=False).head(N)
```

---

### What is GroupBy?

Used to group rows having the same value and perform aggregate operations like:

- mean()
- sum()
- count()
- max()
- min()

---

# Summary

Today I learned:

- Filtering
- Multiple Conditions
- Sorting
- Top N Selection
- GroupBy
- Aggregation
- Basic Business Analysis using Pandas