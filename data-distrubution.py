import numpy
import matplotlib.pyplot as plt

# x = numpy.random.uniform(0.0, 5.0, 100000)
# print(x)

# Histogram
# The histogram graphically shows the following:

# center (i.e., the location) of the data;
# spread (i.e., the scale) of the data;
# skewness of the data;
# presence of outliers; and
# presence of multiple modes in the data.

# plt.hist(x, 100)
# plt.show()

# Normal data distribution
# Values concentrated around a given value is known as normal data distribution or
# the Gaussian data distribution or bell curve.

x = numpy.random.normal(5.0, .1, 100000)
plt.hist(x, 100)
plt.show()