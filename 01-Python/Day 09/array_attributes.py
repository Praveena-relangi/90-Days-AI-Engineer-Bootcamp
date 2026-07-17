import numpy as np

numbers = np.array([10,20,30,40,50])

print(numbers)

# shape always returns tuple
print(numbers.shape)

# dimension
print(numbers.ndim)

# size
print(numbers.size)

# data type
print(numbers.dtype)

# item size
print(numbers.itemsize)

# memory used = size * item size
print(numbers.nbytes)