import numpy
from scipy import stats

# Mean - The average value
# Find the sum of all values and divide the sum by the number of values
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean = numpy.mean(speed)

print("Mean", mean)

# Median - The value in the middle after sorting all the values
median = numpy.median(speed)

print("Median", median)

# Mode - the value that appears the most number of times
mode = stats.mode(speed)
print("Mode", mode[0])
