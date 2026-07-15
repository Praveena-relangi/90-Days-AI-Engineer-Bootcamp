# Day 06 Notes

## File Handling

Python allows storing data permanently using files.

### Open File

```python
open(filename, mode)
```

### Modes

| Mode | Meaning |
|------|---------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| rb | Read Binary |
| wb | Write Binary |

### Read

```python
file.read()
```

### Read One Line

```python
file.readline()
```

### Read Multiple Lines

```python
file.readlines()
```

### Write

```python
file.write()
```

### Best Practice

```python
with open("student.txt","r") as file:
```

Automatically closes the file.

### Real World Uses

- Saving reports
- Logs
- CSV files
- Configuration files
- AI datasets