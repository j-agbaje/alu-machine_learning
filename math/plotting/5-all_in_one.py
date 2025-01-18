#!/usr/bin/env python3
"""
This script generates a set of plots using random data, including a scatter plot,
a line plot, two exponential decay plots, and a histogram. The plots are arranged
in a 3x2 grid.

- The first plot shows the relationship between men's height and weight.
- The second plot displays a cubic curve.
- The third plot represents exponential decay of C-14 over time.
- The fourth plot compares the exponential decay of two radioactive elements (C-14 and Ra-226).
- The fifth plot is a histogram representing student grades.

Modules used:
- numpy: for generating random data and mathematical operations.
- matplotlib.pyplot: for creating the plots.

"""

import numpy as np
import matplotlib.pyplot as plt

# Generate data for the plots
y0 = np.arange(0, 11) ** 3  # Cubic data for the second plot

# Random data for the scatter plot (height vs. weight)
mean = [69, 0]  # Mean height and weight
cov = [[15, 8], [8, 15]]  # Covariance matrix
np.random.seed(5)  # Seed for reproducibility
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T  # Generate random data
y1 += 180  # Adjust weight data

# Exponential decay data for the third plot (C-14)
x2 = np.arange(0, 28651, 5730)  # Time points
r2 = np.log(0.5)  # Decay constant for C-14
t2 = 5730  # Half-life of C-14
y2 = np.exp((r2 / t2) * x2)  # Exponential decay formula

# Exponential decay data for the fourth plot (C-14 and Ra-226)
x3 = np.arange(0, 21000, 1000)  # Time points
r3 = np.log(0.5)  # Decay constant for both elements
t31 = 5730  # Half-life of C-14
t32 = 1600  # Half-life of Ra-226
y31 = np.exp((r3 / t31) * x3)  # C-14 decay
y32 = np.exp((r3 / t32) * x3)  # Ra-226 decay

# Generate random data for the histogram (student grades)
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)  # Grades with mean 68 and stddev 15

# Create a 3x2 grid of subplots
fig, axes = plt.subplots(3, 2)
fig.suptitle("All in One", fontsize="x-small")

# First plot: Scatter plot (height vs. weight)
axes[0, 1].scatter(x1, y1, color='magenta')  # Scatter plot
axes[0, 1].set_xlabel('Height (in)', fontsize='x-small')
axes[0, 1].set_ylabel('Weight (lbs)', fontsize='x-small')
axes[0, 1].set_title("Men's Height vs Weight", fontsize='x-small')
axes[0, 1].set_xticks([60, 70, 80])
axes[0, 1].set_xticklabels(['60', '70', '80'])

# Second plot: Cubic plot
axes[0, 0].plot(y0, c="red")
axes[0, 0].set_xlim(0, 10)
axes[0, 0].set_xticks(np.arange(0, 11, 2))

# Third plot: Exponential decay of C-14
axes[1, 0].plot(x2, y2, color="blue")
axes[1, 0].set_xlim(0, 28650)  # Set x-axis limits
axes[1, 0].set_yscale('log')  # Set y-axis to logarithmic scale
axes[1, 0].set_title("Exponential Decay of C-14", fontsize='x-small')
axes[1, 0].set_ylabel('Fraction Remaining', fontsize='x-small')
axes[1, 0].set_xlabel('Time (years)', fontsize='x-small')
axes[1, 0].set_xticks([0, 10000, 20000])
axes[1, 0].set_xticklabels(['0', '10000', '20000'])

# Fourth plot: Exponential decay of two radioactive elements
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

# Fifth plot: Histogram of student grades
ax5 = fig.add_subplot(3, 1, 3)  # Span the last plot across both columns
bins = np.arange(0, 110, 10)
ax5.hist(student_grades, bins=bins, edgecolor='black')
ax5.set_title("Project A", fontsize="x-small")
ax5.set_xlabel("Grades", fontsize="x-small")
ax5.set_ylabel("Number of Students", fontsize="x-small")
ax5.set_xlim(0, 100)  # Set x-axis limits
ax5.set_ylim(0, 30)  # Set y-axis limits
ax5.set_yticks(np.arange(0, 31, 5))

# Adjust layout for better spacing and display the plot
plt.tight_layout()
plt.show()

