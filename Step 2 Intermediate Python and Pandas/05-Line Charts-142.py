## 2. Introduction To The Data ##

import pandas as pd

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt

# We can make the following observations from the table:
# In 1948:
#        monthly unemployment rate ranged between 3.4 and 4.0.
#        highest unemployment rate was reached in both March and December.
#        lowest unemployment rate was reached in January.
#    From January to March, unemployment rate trended up.
#    From March to May, unemployment rate trended down.
#    From May to August, unemployment rate trended up.
#    From August to October, unemployment rate trended down.
#    From October to December, unemployment rate trended up.

# general workflow is:
#    create a plot using data
#    customize the appearance of the plot
#    display the plot
#    edit and repeat until satisfied

#  If you'd like to follow along on your own computer, we recommend installing matplotlib using Anaconda: conda install matplotlib. We recommend working with matplotlib using Jupyter Notebook because it can render the plots in the notebook itself. You will need to run the following Jupyter magic in a code cell each time you open your notebook: %matplotlib inline. Whenever you call show(), the plots will be displayed in the output cell.

plt.plot()
plt.show()

## 7. Adding Data ##

# Assigned first 12 rows to a variable just for easy reference.
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.show()

## 8. Fixing Axis Ticks ##

first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.show()

## 9. Adding Axis Labels And A Title ##

first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])

plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.show()