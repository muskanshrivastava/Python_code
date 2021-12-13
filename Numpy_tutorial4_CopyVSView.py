import numpy as np
import os

os.system('cls')

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

# The copy SHOULD NOT be affected by the changes made to the original array.
print(arr)
print(x)
print("-"*50)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

# The view SHOULD be affected by the changes made to the original array.
print(arr)
print(x)
print("-"*50)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

# The original array SHOULD be affected by the changes made to the view.
print(arr)
print(x)
print("-"*50)

# Check if Array Owns it's Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

# The copy returns None.
# The view returns the original array.
print(x.base)
print(y.base)
print("-"*50)