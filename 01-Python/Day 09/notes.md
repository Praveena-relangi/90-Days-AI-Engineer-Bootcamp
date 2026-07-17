# Day 09 Notes - Advanced NumPy

## Important Concepts

### reshape()

Rule:

Rows × Columns = Total Elements

Example:

```python
a = np.arange(1,7)
a.reshape(2,3)
```

---

### reshape(-1)

NumPy automatically calculates the missing dimension.

```python
a.reshape(-1,3)
```

---

### flatten()

- Returns a new copy
- Original array remains unchanged

---

### ravel()

- Returns a view (whenever possible)
- More memory efficient than flatten()

---

### transpose (.T)

Rows become columns.

Columns become rows.

Shape changes:

(m,n)

↓

(n,m)

---

### Vectorization

Instead of loops:

```python
salary + 5000
```

NumPy performs operations on the entire array.

---

### Broadcasting

```python
array + 5
```

NumPy behaves as if:

```python
array + [5,5,5,5]
```

But it does NOT create another array in memory.

Advantages:

- Faster
- Memory efficient

---

### Boolean Mask

```python
marks > 75
```

Output:

```python
[True, True, False]
```

---

### Boolean Indexing

```python
marks[marks > 75]
```

Returns only matching elements.

---

## Interview Questions

Difference between flatten() and ravel()

flatten()

- Returns copy
- More memory

ravel()

- Returns view
- Memory efficient

---

Difference between reshape() and transpose()

reshape()

- Changes shape

transpose()

- Swaps rows and columns

---

Why is NumPy faster?

- Continuous memory
- Vectorization
- Broadcasting
- Optimized C implementation

---

## Key Takeaways

✔ Think in arrays, not loops

✔ Broadcasting saves memory

✔ Boolean masks are the foundation of filtering

✔ Vectorization is one of NumPy's biggest strengths