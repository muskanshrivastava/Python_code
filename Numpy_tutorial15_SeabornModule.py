# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# Distplots
# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as plt
import seaborn as sns
import os

os.system('cls')
print('\nSTART FROM HERE')
print('*'*50)

# Plotting a Displot
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Distplot Without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()