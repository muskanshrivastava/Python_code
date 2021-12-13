import numpy as np
import os

os.system("cls")
arr0D = np.array(40)
arr1D = np.array([1,2,3,4,5])
arr2D = np.array([[1,2,3,4,5],[1,2,3,4,5]])
arr3D = np.array([[[1,2,3,4,5],[2,3,4,5,6]],[[3,4,5,6,7],[4,5,6,7,8]]])

print("0-D numpy array : ",arr0D)  # 0-D array
print("-"*50)
print("1-D numpy array : ",arr1D)        # 1-D array
print("-"*50)
print("2-D numpy array :\n",arr2D)     # 2-D array
print("-"*50)
print("3-D numpy array with 2-D array :\n",arr3D)    # 3-D array
print('-'*50)

print("version of numpy : ",np.__version__)
print("Type of numpy array : ",type(arr1D))
print("Another way to initialize numpy array : ",np.array((1,2,3,4,5)))
print('-'*50)

print("Number of dimension : ",arr0D.ndim)
print("Number of dimension : ",arr1D.ndim)
print("Number of dimension : ",arr2D.ndim)
print("Number of dimension : ",arr3D.ndim)
print("-"*50)

# Creating 5-d array

arr5D = np.array([1,2,3,4], ndmin= 5)
print('5-D numpy array',arr5D)
print("Number of dimension : ",arr5D.ndim)
print("-"*50)



