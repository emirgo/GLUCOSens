"""
    Author:         Emirhan Gocturk (460385)
    Description:    GLUCOSens desktop client
    Date:           11 October 2021
"""

from pandas import read_csv
from matplotlib import pyplot
from numpy import arange
from scipy.optimize import curve_fit

def objective(x, a, b):
    return a * x + b

# dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
dataframe = read_csv(url, header=None)
data = dataframe.values
x, y = data[:, 4], data[:, -1]
# curve fit
popt, _ = curve_fit(objective, x, y)
a, b = popt
print('y = %.5f * %.5f' % (a, b))
pyplot.scatter(x, y)
x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b)
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
