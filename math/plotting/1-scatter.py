#!/usr/bin/env python3
"""
This script generates a scatter plot of men's height vs. weight based on a
multivariate normal distribution. The data is created using numpy and visualized
with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


mean = [69, 0]
cov = [[15, 8], [8, 15]]  # Covariance matrix
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# Plot the scatter plot
plt.scatter(x, y, color='magenta')
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title("Men's Height vs Weight")
plt.show()

