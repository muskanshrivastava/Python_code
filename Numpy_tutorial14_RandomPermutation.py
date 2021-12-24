from numpy import random
import numpy as np
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

# Random Permutations of Elements
# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling Arrays
# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
# The shuffle() method makes changes to the original array
arr = np.array([1, 2, 3, 4, 5])
print([1, 2, 3, 4, 5])
random.shuffle(arr)
print("Random Shuffling of a given array : ",arr)
print('-'*100)

# Generating Permutation of Arrays
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
arr = np.array([1, 2, 3, 4, 5])
print([1, 2, 3, 4, 5])
print('Generating Permutation of a given Array : ',random.permutation(arr))
print('-'*100)