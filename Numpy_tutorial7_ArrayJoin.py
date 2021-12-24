import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

#  joining 1D Array
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr1,arr2)
print('joining 1D Array :')
print(arr)
print("-"*50)

# Join two 2-D arrays along rows (axis=1 (Join vertically) )
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr1,"\n",arr2)
print('Join two 2-D arrays along rows :')
print(arr)
print("-"*50)

# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr1,"\n",arr2)
print('Joining Arrays Using Stack Functions :')
print(arr)
print("-"*50)

# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr1,arr2)
print('Joining Arrays Using hstack() (along rows) :')
print(arr)
print("-"*50)

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr1,arr2)
print('Joining Arrays Using vstack() (along columns) :')
print(arr)
print("-"*50)

# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr1,arr2)
print('Joining Arrays Using dstack() (along height) :')
print(arr)
print('Dimension : ',arr.ndim)
print("-"*50)












