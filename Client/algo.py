"""
    Author:         Emirhan Gocturk (460385)
    Description:    GLUCOSens desktop client
    Date:           11 October 2021
"""

from pandas import read_csv
from matplotlib import pyplot

# dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
dataframe = read_csv(url, header=None)
data = dataframe.values
x, y = data[:, 4], data[:, -1]
pyplot.scatter(x, y)
pyplot.show()
