#!/usr/bin/env python3
"""
This script generates multiple plots using matplotlib. 

It includes:
- A scatter plot of height vs. weight for a random sample of data.
- A simple line plot of the cubes of integers from 0 to 10.
- A logarithmic plot of exponential decay for C-14.
- A plot comparing the decay of C-14 and Ra-226 over time.
- A histogram of student grades with specified bins.

The plots are displayed in a 3x2 grid, with the histogram spanning the bottom row.

Dependencies:
- numpy
- matplotlib

"""

import numpy as np
import matplotlib.pyplot as plt

# Generate data
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create figure and axes for multiple plots
fig, axes = plt.subplots(3, 2, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 1, 2]})

# Scatter plot for height vs. weight
axes[0, 1].scatter(x1, y1, color='magenta')
axes[0, 1].set_xlabel('Height (in)', fontsize='x-small')
axes[0, 1].set_ylabel('Weight (lbs)', fontsize='x-small')
axes[0, 1].set_title("Men's Height vs Weight", fontsize='x-small')
axes[0, 1].set_xticks([60, 70, 80])
axes[0, 1].set_xticklabels(['60', '70', '80'])

# Plot cubes of integers from 0 to 10
axes[0, 0].plot(y0, c="red")
axes[0, 0].set_xlim(0, 10)
axes[0, 0].set_xticks(np.arange(0, 11, 2))

# Exponential decay plot for C-14
axes[1, 0].plot(x2, y2, color="blue")
axes[1, 0].set_xlim(0, 28650)
axes[1, 0].set_yscale('log')
axes[1, 0].set_title("Exponential Decay of C-14", fontsize='x-small')
axes[1, 0].set_ylabel('Fraction Remaining', fontsize='x-small')
axes[1, 0].set_xlabel('Time (years)', fontsize='x-small')
axes[1, 0].set_xticks([0, 10000, 20000])
axes[1, 0].set_xticklabels(['0', '10000', '20000'])

# Exponential decay of C-14 and Ra-226
axes[1, 1].plot(x3, y31, color='red', linestyle='--')
axes[1, 1].plot(x3, y32, color='green')
axes[1, 1].set_xlim(0, 20000)
axes[1, 1].set_ylim(0, 1)
axes[1, 1].set_xticks(np.arange(0, 25000, 5000))
axes[1, 1].set_yticks(np.arange(0, 1.5, .5))
axes[1, 1].set_title("Exponential Decay of Radioactive Elements", fontsize='x-small')
axes[1, 1].set_ylabel('Fraction Remaining', fontsize='x-small')
axes[1, 1].set_xlabel('Time (years)', fontsize='x-small')
axes[1, 1].legend(['C-14', 'Ra-226'], loc='upper right', fontsize='x-small')

# Histogram for student grades
ax_hist = fig.add_subplot(3, 1, 3)
bins = np.arange(0, 110, 10)
ax_hist.hist(student_grades, bins=bins, edgecolor='black')
ax_hist.set_xlabel("Grades", fontsize='x-small')
ax_hist.set_ylabel('Number of Students', fontsize='x-small')
ax_hist.set_title("Project A", fontsize='x-small')
ax_hist.set_xlim(0, 100)
ax_hist.set_ylim(0, 30)
ax_hist.set_yticks(np.arange(0, 31, 5))

# Adjust layout and display plot
plt.tight_layout()
plt.show()

