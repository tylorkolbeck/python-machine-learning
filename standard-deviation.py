# Standard deviation - is a number that describes how spread out values are.
# A lower standard deviation means the most of the valuse are close to the mean(average) value.
import numpy

speed = [86, 87, 88, 86, 87, 85, 86]

std = numpy.std(speed)
print(std)

# Variance - a number that indicates how spread out the values are.
# standard deviation = the square root of variance
# standard deviation** = variance

# (32+111+138+28+59+77+97) / 7 = 77.4 <<< the mean

# for each value find the difference from the mean
#  32 - 77.4 = -45.4
# 111 - 77.4 =  33.6
# 138 - 77.4 =  60.6

# For each difference find the square value
# (-45.4)2 = 2061.16
#  (33.6)2 = 1128.96
#  (60.6)2 = 3672.36

# The variance is the average number of these squared differences:
# (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2)

speed2 = [150, 87, 88, 100, 87, 85, 0]
variance = numpy.var(speed2)

print(variance)

# Symbols
# Standard Deviation is often represented by the symbol Sigma: σ
# Variance is often represented by the symbol Sigma Square: σ2