import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
# Note: The return value is an array containing three arrays.
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(arr)
print("Splitting 1D Array : ")
print(newarr)
print('-'*50)

# Split the array in 4 parts
# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example below, array_split() worked properly but split() would fail.
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(arr)
print('Splitting array into 4 parts : ')
print(newarr)
print('-'*50)

# The return value of the array_split() method is an array containing each of the split as an array.
# If you split an array into 3 arrays, you can access them from the result just like any array element
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(arr)
print("Accessing splitted array : ")
print(newarr[0])
print(newarr[1])
print(newarr[2])
print('-'*50)

# Splitting 2-D Arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(arr)
print('Splitting 2D array : ')
print(newarr)
print("Accessing splitted array : ")
print(newarr[0])
print(newarr[1])
print(newarr[2])
print('-'*50)

# Split the 2-D array into three 2-D arrays along rows.
# hsplit() would do same split as it is.
# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(arr)
print('Spltting 2-D array into three 2-D arrays along rows : ')
print(newarr)
print("Accessing splitted array : ")
print(newarr[0])
print(newarr[1])
print(newarr[2])



