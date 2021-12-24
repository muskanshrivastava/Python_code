import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
# The searchsorted() method is assumed to be used on sorted arrays.
# Find the indexes where the value 7 should be inserted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(arr)
print('Index of searched element : ',x)
print('-'*50)

# Search From the Right Side
# By default the left most index is returned, but we can give side='right' to return the right most index instead.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(arr)
print('Search From the Right Side : ', x)
print('-'*50)

# Find the indexes where the values 2, 4, and 6 should be inserted    
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 8, 10])
print(arr)
print('the indexes where the values 2, 4, and 6 should be inserted : ')
print(x) 





