# R-squared
# Linear regression can only be used if there is a relationship between the values
# of the x-axis and the y-axis.  This is called r-squared.
# R-squared value ranges from 0 to 1 where 0 means no relationship and 1 is 100%
# related.

# You can compute the r-squared value using stats.linregress(x,y) which returns r
# slope, intercept, r, p, std_err = stats.linregress(x,y)
# print(r)

# Regression - regression is used when you try to find the relationship between variables
# In machine learning and in statistical modeling that relationship is used to predict the
# outcome of future events.

# Linear regression - the relationship between the data-points to draw a straight line through all them.
import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myFunc(x):
    return slope * x + intercept


mymodel = list(map(myFunc, x))

print("R-squared", r)  # -0.76
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Predict Future Values
predict = myFunc(10)

print("Predict 10", predict)
