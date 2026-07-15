# Day 05 Notes

## Object Oriented Programming (OOP)

OOP is a programming paradigm that organizes code using objects.

### Class

Blueprint of an object.

Example:

```python
class Student:
    pass
```

### Object

Instance of a class.

```python
s1 = Student()
```

### Constructor

```python
def __init__(self):
```

Automatically executes while creating object.

### Attributes

Variables inside objects.

```python
self.name
self.age
```

### Methods

Functions inside class.

```python
def display(self):
```

### self

Represents the current object.

### Real World Example

Class → Car

Objects →

- BMW
- Audi
- Tesla

Each object has

- color
- model
- speed

Each object can

- start()
- stop()
- accelerate()