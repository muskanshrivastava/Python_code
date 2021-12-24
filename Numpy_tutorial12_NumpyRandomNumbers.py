# Random Numbers in NumPy
# Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.
# If there is a program to generate random number it can be predicted, thus it is not truly random.
# Random numbers generated through a generation algorithm are called pseudo random.

# Generate Random Number
# NumPy offers the random module to work with random numbers.
# Generate a random integer from 0 to 100

from numpy import random
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

x = random.randint(100)
print('Generating random integer value (1-100) : ',x)
print('-'*50)

# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.
x = random.rand()
print('Generating random float value (0-1) : ',x)
print('-'*50)

# Generate Random Array
# The randint() method takes a size parameter where you can specify the shape of an array.
# Generate a 1-D array containing 5 random integers from 0 to 100
x=random.randint(100, size=(5))
print('Generating 1D integer Array (1-100) : ',x)
print('-'*50)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
x = random.randint(100, size=(3, 5))
print('Generating 2D integer Array (1-100) :\n',x)
print('-'*50)

# Floats
# The rand() method also allows you to specify the shape of the array.
# Generate a 1-D array containing 5 random floats
x = random.rand(5)
print('Generating 1D float Array of 5 elements : ',x)
print('-'*50)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers
x = random.rand(3, 5)
print('Generating 2D float Array  :\n',x)
print('-'*50)

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.
x = random.choice([3, 5, 7, 9])
print('Generating Random Number From Array : ',x)

# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(' Generate a 2-D array from the given array :\n',x)

