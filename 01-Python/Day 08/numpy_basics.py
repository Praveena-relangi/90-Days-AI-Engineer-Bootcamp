import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Hello Praveena")
print(numbers)
print(type(numbers))

# Difference between python list and numpy array
python_list = [10,20,30,40,50]

numpy_array = np.array([10,20,30,40,50])

print(type(python_list))
print(type(numpy_array))

# printing individual array elements
print(numbers[0])
print(numbers[2])
print(numbers[4])

# negative indexing
print(numbers[-1])
print(numbers[-2])

# changing elements
numbers[2]=100
print(numbers)

# Length of numpy array
print(len(numbers))