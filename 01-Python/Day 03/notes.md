# 📝 Day 3 Notes - Decision Making in Python

## 📌 What is Decision Making?

Decision Making is the process of executing different blocks of code based on whether a condition evaluates to **True** or **False**.

Example:

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

## 📌 Flow of Execution

Python executes statements from **top to bottom**.

When conditional statements are used, the execution flow changes depending on whether the condition is **True** or **False**.

---

## 📌 Code Block

A code block is a group of statements that have the same indentation.

Example:

```python
if age >= 18:
    print("Eligible")
    print("Welcome")
```

Both `print()` statements belong to the same code block.

---

## 📌 Indentation

Python uses **indentation** instead of curly braces `{}`.

Indentation:

- Improves code readability.
- Defines code blocks.
- Is mandatory in Python.

Incorrect indentation results in an **IndentationError**.

---

# 📌 if Statement

### Syntax

```python
if condition:
    statement
```

### Purpose

Used when a block of code should execute **only if the condition is True**.

### Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

# 📌 if...else Statement

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Purpose

Used when one action should execute if the condition is **True**, and another action should execute if the condition is **False**.

### Example

```python
marks = 40

if marks >= 35:
    print("Pass")
else:
    print("Fail")
```

---

# 📌 if...elif...else Statement

### Syntax

```python
if condition1:
    statement

elif condition2:
    statement

elif condition3:
    statement

else:
    statement
```

### Purpose

Used when there are **multiple independent conditions** to check.

### Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 35:
    print("Grade D")

else:
    print("Fail")
```

### Important Rule

Python checks conditions from **top to bottom**.

Once it finds the **first True** condition, it executes that block and skips the remaining `elif` and `else` blocks.

---

# 📌 Nested if Statement

### Definition

A Nested `if` means placing one `if` statement inside another `if` statement.

### Syntax

```python
if condition1:

    if condition2:
        statement
```

### Example

```python
age = 20

if age >= 18:

    marks = 80

    if marks >= 75:
        print("Admission Approved")
```

### Important Rule

The inner `if` executes **only if the outer `if` condition is True**.

---

# 📌 Nested if...else Statement

### Definition

Nested `if...else` means placing a complete `if...else` statement inside another `if` or `else` block.

### Syntax

```python
if condition1:

    if condition2:
        statement
    else:
        statement

else:
    statement
```

### Example

```python
age = 20

if age >= 18:

    marks = 80

    if marks >= 75:
        print("Admission Approved")
    else:
        print("Marks are insufficient.")

else:
    print("Age is not eligible.")
```

---

# 📌 Difference Between if, if...else and if...elif...else

| Statement | Purpose |
|-----------|---------|
| if | Executes only when the condition is True |
| if...else | Executes one of two possible blocks |
| if...elif...else | Chooses one block from multiple independent conditions |

---

# 📌 Difference Between if...elif...else and Nested if

| if...elif...else | Nested if |
|------------------|-----------|
| Independent conditions | Dependent conditions |
| Only one block executes | Inner condition depends on the outer condition |
| Used for categorization | Used for step-by-step verification |

---

# 📌 Real-World Examples

### if Statement

- Voting Eligibility
- High Score Checker
- Positive Number Checker

### if...else Statement

- ATM PIN Verification
- Login Authentication
- Pass or Fail
- Movie Ticket Eligibility

### if...elif...else Statement

- Student Grade Calculator
- Traffic Signal System
- Temperature Checker
- BMI Calculator
- Salary Category

### Nested if

- Driving License Process
- ATM Withdrawal
- Scholarship Approval
- Bank Account Opening
- Hiring Process
- Airport Security Check

---

# 📌 Common Mistakes

- Forgetting the colon (`:`).
- Incorrect indentation.
- Using `=` instead of `==`.
- Writing lower-priority conditions before higher-priority conditions.
- Confusing Nested `if` with `if...elif...else`.
- Assuming the inner `if` executes even when the outer `if` is False.

---

# 📌 Interview Tips

- Start with the definition.
- Explain how the execution flow works.
- Mention when the concept should be used.
- Give one or two real-world examples.
- Use simple language.
- Differentiate between similar concepts whenever possible.

---

# 📌 Key Takeaways

- Decision Making helps programs choose different execution paths.
- Python uses indentation to define code blocks.
- `if` is used for a single condition.
- `if...else` is used when there are two possible outcomes.
- `if...elif...else` is used for multiple independent conditions.
- Nested `if` is used when conditions depend on each other.
- Nested `if...else` is useful for multi-step verification systems.
- Python evaluates conditions from top to bottom.
- Always write higher-priority conditions before lower-priority conditions.
- Practice real-world problems to improve logical thinking.

---

# 📌 Programs Created Today

## if Statement

- Voting Eligibility Checker
- Adult Checker
- Positive Number Checker
- Even Number Checker
- High Score Checker

## if...else Statement

- Voting Eligibility
- Even or Odd Checker
- Pass or Fail Checker
- Positive or Negative Checker
- Password Validation

## if...elif...else Statement

- Student Grade Calculator
- Age Category Checker
- Traffic Signal System
- Temperature Checker
- BMI Category Calculator

## Nested if

- College Admission
- ATM Transaction
- Scholarship Eligibility
- Movie Booking
- Office Login

## Practice Challenges

- Driving License
- Laptop Purchase
- Gym Membership

## Mini Projects

- Movie Ticket Booking System
- Student Report Card System
- Smart Bank Account Opening System

---

# 🎯 Day 3 Summary

Today I learned how Python makes decisions using conditional statements. I understood the differences between `if`, `if...else`, `if...elif...else`, and Nested `if`. I also practiced solving real-world problems and mini projects using decision-making concepts.

---

## ✅ Day 3 Status

**Completed Successfully 🎉**

### 🚀 Next Topic

**Day 4 – Loops in Python**

- for Loop
- while Loop
- range()
- Nested Loops
- Pattern Printing
- Multiplication Tables
- Real-world Loop Problems
- Mini Projects