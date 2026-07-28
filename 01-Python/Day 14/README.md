# 📅 Bootcamp Week 2 – Day 14

# 📌 Topic
Data Manipulation using Pandas

---

# 🎯 Objectives

In this session, I learned how to manipulate datasets using Pandas to extract meaningful information.

Topics covered:

- Filtering rows
- Applying multiple conditions
- Sorting data
- Selecting Top N records
- Grouping data
- Basic data analysis

---

# 🧠 Concepts Learned

## 1. Filtering Data

Retrieve rows based on conditions.

Example:

```python
df[df["Department"] == "HR"]
```

---

## 2. Multiple Conditions

Using logical operators.

AND

```python
(df["Department"] == "IT") & (df["Salary"] > 50000)
```

OR

```python
(df["Department"] == "IT") | (df["Department"] == "HR")
```

---

## 3. Sorting

Sort data based on columns.

```python
df.sort_values("Salary", ascending=False)
```

---

## 4. Top Records

Retrieve highest values.

```python
df.sort_values("Salary", ascending=False).head(3)
```

---

## 5. Group By

Aggregate data by categories.

```python
df.groupby("Department")["Salary"].mean()
```

---

## 6. Count Records

```python
df.groupby("Department")["Salary"].count()
```

---

# 💻 Practice

Implemented:

- HR employee filtering
- Salary filtering
- Sorting salaries
- Top 2 highest-paid employees
- Department-wise average salary
- Employee count
- Experience filtering
- Column selection
- Interview-style filtering challenge

---

# 📚 Key Takeaways

- Filtering is one of the most frequently used Pandas operations.
- Multiple conditions allow complex data queries.
- Sorting helps identify top and bottom records.
- GroupBy enables data aggregation.
- Pandas can answer business questions with very little code.

---

# 🚀 Next Step

Week 2 Capstone Project

A complete Data Analysis project combining:

- Pandas
- NumPy
- Matplotlib
- Data Cleaning
- Business Insights

---

⭐ AI Engineer Bootcamp