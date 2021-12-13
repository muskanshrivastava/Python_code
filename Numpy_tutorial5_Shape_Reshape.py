import numpy as np
import os

os.system('cls')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
# The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.
print(arr.shape)
print("-"*50)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
print("-"*50)

# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print("-"*50)

# Reshape From 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
print("-"*50)

# Check if the returned array is a copy or a view
# The example below returns the original array, so it is a view.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
print("-"*50)

# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# Note: We can not pass -1 to more than one dimension.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
print("-"*50)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
print("-"*50)






