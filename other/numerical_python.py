"""
simple exercise to test numpy
"""

import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = np.array(a)
print(b)

z = np.zeros(5)
print(z)
print(type(z))

z2 = np.random.randint(10, size=10)
print(z2)
