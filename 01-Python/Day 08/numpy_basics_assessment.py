import numpy as np

#creating a numpy array
numpy_array = np.array([5,10,15,20,25])

#print elements
print("First element of the array is: ", numpy_array[0])
print("Last element of the array is: ", numpy_array[len(numpy_array)-1])
print("Third element of the array is: ", numpy_array[2])

# change 15 to 100
numpy_array[2] = 100
print(numpy_array)
print("numpy_array[2]: ", numpy_array[2])

# print length of array and the data type
print("The length of numpy_array is: ", len(numpy_array))
print("The type of numpy_array is: ", type(numpy_array))