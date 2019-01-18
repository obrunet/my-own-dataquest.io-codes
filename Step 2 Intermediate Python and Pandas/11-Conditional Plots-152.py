## 2. Introduction to the Data Set ##

# In this mission, we'll explore how to quickly create multiple plots that are subsetted using one or more conditions.

# We'll be working with the seaborn visualization library, which is built on top of matplotlib. Seaborn has good support for more complex plots, attractive default styles, and integrates well with the pandas library. Here are some examples of some complex plots that can be created using seaborn:

import pandas as pd

titanic = pd.read_csv('train.csv')
titanic = titanic[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
titanic = titanic.dropna(axis=0)

## 3. Creating Histograms In Seaborn ##

# Seaborn works similarly to the pyplot module from matplotlib. We primarily use seaborn interactively, by calling functions in its top level namespace. Like the pyplot module from matplotlib, seaborn creates a matplotlib figure or adds to the current, existing figure each time we generate a plot. When we're ready to display the plots, we call pyplot.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Use the seaborn.distplot() function to visualize the distribution of the "Age" column.
sns.distplot(titanic['Age'])

plt.show()

## 4. Generating A Kernel Density Plot ##

# While having both the histogram and the kernel density plot is useful when we want to explore the data, it can be overwhelming for someone who's trying to understand the distribution. To generate just the kernel density plot, we use the seaborn.kdeplot() function

sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')
plt.show()

# While the distribution of data is displayed in a smoother fashion, it's now more difficult to visually estimate the area under the curve using just the line chart. When we also had the histogram, the bars provided a way to understand and compare proportions visually.



## 5. Modifying The Appearance Of The Plots ##

sns.set_style('white')
sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')

#To remove the axis spines for the top and right axes, we use the seaborn.despine() function.By default, only the top and right axes will have their spines removed. To despine the other two axes, we need to set the left and bottom parameters to True
sns.despine(left=True, bottom=True)

plt.show()

## 6. Conditional Distributions Using A Single Condition ##

# In seaborn, we can create a small multiple by specifying the conditioning criteria and the type of data visualization we want.

# Use a FacetGrid instance to generate three plots on the same row:
# One for each unique value of Pclass.
# Each plot should be a kernel density plot of the "Age" column, with the area under the curve shaded.
# Each plot should have a height of 6 inches.

#grid of plots that displays the age distributions for each class.
g = sns.FacetGrid(titanic, col='Pclass', size=6)
# For each subset of values, generate a kernel density plot of the 'Age' columns.
g.map(sns.kdeplot, 'Age', shade=True)

#The function that's passed into FacetGrid.map() has to be a valid matplotlib or seaborn function. For example, we can map matplotlib histograms to the grid: g.map(plt.hist, "Age")

sns.despine(left=True, bottom=True)
plt.show()

## 7. Creating Conditional Plots Using Two Conditions ##

# We can use two conditions to generate a grid of plots, each containing a subset of the data with a unique combination of each condition. When creating a FacetGrid, we use the row parameter to specify the column in the dataframe we want used to subset across the rows in the grid. The best way to understand this is to see a working example.

g = sns.FacetGrid(titanic, col="Pclass", row="Survived")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()
# Try changing the conditions to see the resulting plots.

## 8. Creating Conditional Plots Using Three Conditions ##

# When subsetting data using two conditions, the rows in the grid represented one condition while the columns represented another. We can express a third condition by generating multiple plots on the same subplot in the grid and color them differently. Thankfully, we can add a condition just by setting the hue parameter to the column name from the dataframe.

#Let's add a new condition to the grid of plots we generated in the last step and see what this grid of plots would look like.

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue='Sex', size=3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

# Now that we're coloring plots, we need a legend to keep track of which value each color represents.

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue='Sex', size=3)

# Add a legend for the hues representing the values in the Sex column
# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid
g.map(sns.kdeplot, "Age", shade=True).add_legend()

sns.despine(left=True, bottom=True)
plt.show()