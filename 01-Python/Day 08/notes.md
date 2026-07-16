# Day 08 Notes - NumPy Basics

# What is NumPy?

NumPy (Numerical Python) is a Python library used for fast numerical computations.

It provides a special data structure called ndarray.

---

# Why NumPy?

Python Lists

- Slow
- More memory
- Elements stored separately

NumPy Arrays

- Faster
- Less memory
- Continuous memory allocation
- Optimized C implementation

---

# Import NumPy

```python
import numpy as np
```

np is an alias.

---

# Create Array

```python
import numpy as np

numbers = np.array([10,20,30,40,50])
```

Output

```
[10 20 30 40 50]
```

---

# Data Type

```python
print(type(numbers))
```

Output

```
<class 'numpy.ndarray'>
```

---

# Access Elements

```python
print(numbers[0])
print(numbers[2])
```

Output

```
10
30
```

---

# Negative Indexing

```python
print(numbers[-1])
```

Output

```
50
```

---

# Modify Elements

```python
numbers[2]=100
```

Output

```
[10 20 100 40 50]
```

---

# Length

```python
len(numbers)
```

Output

```
5
```

---

# Useful pip Commands

Install NumPy

```bash
pip install numpy
```

Installed Packages

```bash
pip list
```

Package Information

```bash
pip show numpy
```

requirements.txt

```bash
pip freeze > requirements.txt
```

---

# Important Points

- NumPy Array = ndarray
- Faster than Python List
- Continuous Memory Allocation
- Supports Broadcasting
- Used in AI & ML

---

# Interview Questions

### What is NumPy?

A Python library used for numerical computing and array operations.

---

### Why is NumPy faster than Python Lists?

Because NumPy stores data in continuous memory blocks and performs operations using optimized C code.

---

### What is ndarray?

N-dimensional array provided by NumPy.

---

### What is the alias generally used while importing NumPy?

```python
import numpy as np
```

---

### Where is NumPy used?

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Data Science
- Computer Vision
- Image Processing

---

# Day 08 Summary

- Installed NumPy
- Created virtual environment
- Created NumPy arrays
- Accessed array elements
- Modified array elements
- Learned ndarray
- Understood why NumPy is faster than Python Lists

✅ Day 08 Completed