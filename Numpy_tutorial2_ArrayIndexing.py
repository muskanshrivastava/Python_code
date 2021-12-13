import numpy as np
import os

os.system("cls")

arr = np.array([1,2,3,4,5])
print("First element of array : ",arr[0]) # Forward indexing
print('Sum of {} and {} : '.format(arr[2],arr[3]),arr[2] + arr[3])
print('-'*50)

# Traversing in 2-D array
arr2D = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2D)
print("Second element of first row : ",arr2D[0,1])
print('-'*50)

# Traversing in 3-D array
arr3D = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(arr3D)
print('Element from 3D array : ', arr3D[1,1,2])
print('-'*50)

# Negative Indexing
print(arr2D)
print("Last element of 2D array : ", arr2D[1,-1])
print("-"*50)

# Slicing in 2D array
print(arr2D)
print("2D Array Slicing : ",arr2D[1, 1:4])
print(arr2D[0:2, 1:4])
