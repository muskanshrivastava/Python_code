import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
arr = np.array([41, 42, 43, 44])
x = arr[[True, False, True, False]]
print(arr)
print('Filtering Array : ', x)
print('-'*50)

# Create a filter array that will return only values higher than 42
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(arr)
print(filter_arr)
print('Filtering Array : ',newarr)
print('-'*50)

# Create a filter array that will return only values higher than 42
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(arr)
print(filter_arr)
print('Filtering Directly from the given Array : ',newarr)
print('-'*50)

# Create a direct filter array that will return only even elements from the original array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(arr)
print(filter_arr)
print('Filtering even elements Directly from the given Array : ', newarr)
print('-'*50)


