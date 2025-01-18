#!/usr/bin/env python3
"""
This script plots the exponential decay of Carbon-14 (C-14) using the
exponential decay formula. It uses a logarithmic scale for the y-axis.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
x = np.arange(0, 28651, 5730)  
r = np.log(0.5)  
t = 5730  


y = np.exp((r / t) * x)

# your code here
plt.plot(x, y, color="blue")
plt.xlim(0, 28650)  # Set x-axis limits
plt.yscale('log')  # Set y-axis to logarithmic scale
plt.title("Exponential Decay of C-14")
plt.ylabel('Fraction Remaining')
plt.xlabel('Time (years)')

# Display the plot
plt.show()

