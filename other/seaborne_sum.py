"""
This is a program to show the implementation of the seaborn library.
"""

import matplotlib
matplotlib.use('tkagg')
from matplotlib import pyplot as plt
import seaborn as sns

# Creating a simple list to plot

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [x**2 for x in x]

sns.set_style("darkgrid")
line_plot = sns.scatterplot(x, y)

#sns.relplot(kind="line")

plt.show()
