import numpy as np

#data type
a = np.array([True, 2.5, 7])
print(a)
print(a.dtype)

#Reshape - 2D
numbers = np.array([1,2,3,4,5,6])
print(numbers)
numbers = numbers.reshape(2,3)
print(numbers)

# Reshape 3D
a = np.arange(1,13)
print(a)
a = np.arange(1,13)
print(a)

# flatten() & ravel()
a=np.array([[1,2,3],[4,5,6]])
print(a.flatten())
print(a.ravel())

# Transpose
a=np.array([[1,2,3],[4,5,6]])
print(a.T)

# Vectorization
salary = np.array([25000,30000,40000,50000,60000])
print(salary + 5000)

# Broadcasting
numbers = np.array([10,20,30,40])
print(numbers + 2)

# Mathematical functions
marks = np.array([80,90,70,60])
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(np.std(marks))

# Most powerful feature
marks=np.array([80,90,70])
print(marks>75)