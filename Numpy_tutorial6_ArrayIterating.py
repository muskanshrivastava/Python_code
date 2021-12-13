import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)
# Iterating 1D array
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
print("-"*50)

# Iterating 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

print()
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y, end = ' ')
print('\n',"-"*50)

# Iterating 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x, end = ' ')

print('\n')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z, end = ' ')
print('\n',"-"*50)

# Iterating on Each Scalar Element
# In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
print('\n')
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x, end = ' ')
print('\n',"-"*50)

# Iterating Array With Different Data Types
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x,end=' ')
print('\n',"-"*50)

# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x,end=' ')
print('\n',"-"*50)

# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
print("-"*50)