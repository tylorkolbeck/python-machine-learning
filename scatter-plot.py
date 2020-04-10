# Scatter plots is a diagram where each value in the data set is represented by a dot.
# Matplotlib takes two arrays of the same length with one array being the x-axis,
# and the other for the y-axis

import matplotlib.pyplot as plt
import numpy

x = numpy.random.normal(5.0, 1.0, 1000)  # mean 5.0 std 1.0
y = numpy.random.normal(10.0, 2.0, 1000)  # mean 10.0 std 2.0

plt.scatter(x, y)
plt.show()