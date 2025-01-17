#!/usr/bin/env python3
"""
This script generates cubic values from 0 to 10 and plots them using matplotlib.
It uses numpy to calculate the cubic values and matplotlib to create the plot.
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plotting the cubic values
plt.plot(y, c="red")
plt.xlim(0, 10)
plt.show()

