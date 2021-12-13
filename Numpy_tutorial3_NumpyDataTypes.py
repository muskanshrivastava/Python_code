# Data types in numpy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np
import os

os.system('cls')

arr = np.array([1, 2, 3, 4], dtype='S') # Creating array of string type
print(arr)
print(arr.dtype)
print("-"*50)

arr = np.array([1, 2, 3, 4], dtype='i4') # Creating array of 4bytes (int32)
print(arr)
print(arr.dtype)
print("-"*50)

arr = np.array([1.1, 2.1, 3.1]) # Converting  float array into integer array
newarr = arr.astype('i')  # 2nd way : newarr = arr.astype(int) 
print(newarr)
print(newarr.dtype)
print("-"*50)