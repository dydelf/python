"""
matplotlib visualisation training
"""

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(input_value, squares, linewidth=5)

# Set chart title and label axis
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
