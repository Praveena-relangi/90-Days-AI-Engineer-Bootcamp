# 📝 Day 2 Notes - Python Basics: Type Conversion & Operators

## 📅 Date
Day 2 of the 90 Days AI Engineer Bootcamp

---

# 📚 Topics Learned

1. Type Conversion
2. Arithmetic Operators
3. Comparison Operators
4. Logical Operators

---

# 🔄 Type Conversion

## What is Type Conversion?

Type Conversion is the process of converting one data type into another.

Python provides built-in functions for conversion.

### Common Conversion Functions

```python
int()
float()
str()
bool()
```

### Examples

```python
age = int("25")
height = float("5.4")
marks = str(95)
```

---

## Important Points

- `input()` always returns a **String**.
- Convert user input whenever numerical calculations are required.
- Use `type()` to verify the data type.

Example:

```python
age = input("Enter Age: ")

print(type(age))
```

Output

```python
<class 'str'>
```

---

# ➕ Arithmetic Operators

Used to perform mathematical calculations.

| Operator | Description |
|----------|-------------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Floor Division |
| % | Modulus |
| ** | Exponentiation |

### Examples

```python
10 + 5
10 - 5
10 * 5
10 / 5
10 // 3
10 % 3
2 ** 3
```

---

## Difference Between `/` and `//`

### Division (/)

Returns the quotient.

```python
10 / 3
```

Output

```text
3.333333333
```

---

### Floor Division (//)

Returns the floor value of the quotient.

```python
10 // 3
```

Output

```text
3
```

---

## Modulus (%)

Returns the remainder after division.

Example

```python
15 % 4
```

Output

```text
3
```

---

## Exponent (**)

Returns the power.

Example

```python
3 ** 4
```

Output

```text
81
```

---

# 🔍 Comparison Operators

Comparison Operators compare two values and always return a Boolean value.

| Operator | Meaning |
|----------|---------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

### Examples

```python
10 == 10
20 > 15
15 <= 15
```

Output

```text
True
True
True
```

---

## Difference Between `=` and `==`

### =

Assignment Operator

Assigns a value to a variable.

Example

```python
name = "Praveena"
```

---

### ==

Comparison Operator

Compares two values.

Example

```python
name == "Praveena"
```

---

# 🔗 Logical Operators

Logical Operators combine multiple conditions.

## AND

Returns **True** only when all conditions are True.

Example

```python
age >= 18 and has_degree == "yes"
```

---

## OR

Returns **True** if at least one condition is True.

Example

```python
email == "yes" or phone == "yes"
```

---

## NOT

Returns the opposite Boolean value.

Example

```python
not True
```

Output

```text
False
```

---

# 🌍 Real-world Examples

## Arithmetic Operators

- Shopping Bill Calculation
- Student Percentage
- Average Marks
- BMI Calculation

---

## Comparison Operators

- Voting Eligibility
- Pass/Fail Check
- Salary Eligibility
- Highest Marks

---

## Logical Operators

- Login using Email OR Phone
- College Admission Eligibility
- Job Eligibility
- Prime Membership Eligibility
- Face Unlock
- Loan Approval

---

# 💻 Mini Project

## College Admission Eligibility Checker

Concepts Used

- Variables
- User Input
- Type Conversion
- Comparison Operators
- Logical Operators
- if...else Statement

Conditions

- Age >= 17
- Marks >= 75
- Entrance Qualified = yes

---

# 🎤 Interview Questions Practiced

1. Difference between `/` and `//`
2. Difference between `=` and `==`
3. Difference between `>` and `>=`
4. Difference between Comparison and Logical Operators
5. What does `%` do?
6. What does `**` do?
7. Difference between AND, OR and NOT
8. Real-world applications of Operators

---

# 💡 Key Learnings

✅ Type Conversion is necessary because `input()` returns a String.

✅ Arithmetic Operators perform mathematical calculations.

✅ Comparison Operators compare values and return Boolean outputs.

✅ Logical Operators combine multiple conditions.

✅ These concepts are widely used in real-world software applications.

---

# 📌 Best Practices Learned

- Use meaningful variable names.
- Verify data types using `type()`.
- Write readable output messages.
- Use `snake_case` for variable names.
- Think about real-world applications while writing code.

---

# 🚀 Next Topic

Day 3

- if Statement
- if...else
- if...elif...else
- Nested if
- Grade Calculator
- ATM Withdrawal System
- Login Authentication
- Mini Projects

---

> **"Strong fundamentals build strong AI Engineers."**
