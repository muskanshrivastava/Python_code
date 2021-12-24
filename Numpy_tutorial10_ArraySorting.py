import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

# Sorting Arrays
# Note: This method returns a copy of the array, leaving the original array unchanged.
arr = np.array([3, 2, 0, 1])
print(arr)
print('Sorting 1D Array : ',(np.sort(arr)))
print('-'*50)

# Sort a 2-D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(arr)
print('Sorting 2D Array : ')
print(np.sort(arr))
print('-'*50)

# This function returns an array of indices of the same shape as 'a', which would sort the array.
arr = np.array([5,4,3,1,2,7,8,6]) 
print('Indices of elements which should be sorted in this order :\n',np.argsort(arr))