# ----------------------- UNIFORM DISTRIBUTION -----------------------------

import os
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

os.system('cls')
print('-'*20,'STARTS FROM HERE','-'*20)
print()

# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers.
# It has three parameters:
# a - lower bound - default 0 .0.
# b - upper bound - default 1.0.
# size - The shape of the returned array.

# Create a 2x3 uniform distribution 
x = random.uniform(size=(2, 3))
print(x)
print('-'*50)

# Visualization of Uniform Distribution
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
print('-'*50)


