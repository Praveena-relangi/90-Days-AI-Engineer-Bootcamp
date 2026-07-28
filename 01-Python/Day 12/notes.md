# Day 12 Notes - Matplotlib Basics

# Import

```python
import matplotlib.pyplot as plt
```

Matplotlib is used for data visualization.

---

# Line Chart

Used for showing trends over time.

```python
plt.plot(x, y)
```

Customize:

```python
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()
```

Extra customization

```python
color=""
marker=""
linestyle=""
```

---

# Bar Chart

Used for comparing categories.

```python
plt.bar(categories, values)
```

Customize

```python
color=""
width=
```

---

# Pie Chart

Used for showing percentage contribution.

```python
plt.pie(values)
```

Useful parameters

```python
labels=
autopct="%1.1f%%"
explode=
shadow=True
startangle=90
```

---

# Histogram

Used for understanding data distribution.

```python
plt.hist(data)
```

Useful parameters

```python
bins=
color=
edgecolor=
```

A histogram groups continuous numerical values into ranges called bins.

---

# Scatter Plot

Used for understanding relationships between two numerical variables.

```python
plt.scatter(x, y)
```

Useful parameters

```python
color=
s=
```

---

# Which Chart Should I Use?

| Situation | Chart |
|------------|--------|
| Monthly Sales | Line Chart |
| Department-wise Employees | Bar Chart |
| Market Share | Pie Chart |
| Student Marks Distribution | Histogram |
| Study Hours vs Marks | Scatter Plot |

---

# Important Interview Questions

## Difference between Line Chart and Bar Chart

Line Chart

- Shows trends over time

Bar Chart

- Compares categories

---

## Difference between Bar Chart and Histogram

Bar Chart

- Categorical Data
- Bars have gaps

Histogram

- Continuous Numerical Data
- Bars touch each other

---

## Why Scatter Plot?

Used to identify relationships, correlations and outliers between numerical variables.

---

# Key Takeaways

✔ Line Chart → Trends

✔ Bar Chart → Categories

✔ Pie Chart → Percentage Contribution

✔ Histogram → Distribution

✔ Scatter Plot → Relationship between Variables