## 1. Introduction ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt') # depreciated use read_csv instead
houses.head()
houses['Land Slope'].value_counts().sort_index()
scale_land = 'ordinal'
houses['Roof Style'].value_counts().sort_index()
scale_roof = 'nominal'
houses['Kitchen AbvGr'].value_counts().sort_index()
kitchen_variable = 'discrete'

## 2. The Mode for Ordinal Variables ##

def array_mode_func(val_array):
    # returns the mode of an array
    # the mode is the most frequent value in the distribution, not the frequency of that value
    dict = {}
    for val in val_array:
        if val not in val_array:
            dict[val] = 1
        else:
            dict[val] += 1
    # gets the key of the max value of a dict
    return max(dict, key = dict.get)

mode_function = array_mode_func(houses['Land Slope'])
mode_method = houses['Land Slope'].mode()
same = mode_function == mode_method

## 4. The Mode for Discrete Variables ##

houses['Bedroom AbvGr'].unique()
bedroom_variable ='discrete'
bedroom_mode = houses['Bedroom AbvGr'].mode()

houses['SalePrice'].unique()
price_variable = 'continuous'

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)

mode = 150000 # midpoint
mean = houses['SalePrice'].mean()
median = houses['SalePrice'].median()
sentence_1 = True
sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}
# When we plot a histogram or a kernel density plot to visualize the shape of a distribution, 
#the mode will always be the peak of the distribution. 
shape_1='right skew'
shape_2='right skew'
shape_3='left skew'

## 7. Symmetrical Distributions ##

import matplotlib.pyplot as plt

# kernel density plot for this distribution using Series.plot.kde()
houses['Mo Sold'].plot.kde(xlim=(1,12)) # The lower boundary of the x-axis is 1 and the upper one 12

# plots three vertical lines
plt.axvline(houses['Mo Sold'].mode()[0],color='Green',label='Mode')
plt.axvline(houses['Mo Sold'].median(),color='Orange',label='Median')
plt.axvline(houses['Mo Sold'].mean(),color='Black',label='Mean')
plt.legend() # displays all the labels using a legend


# In this mission, we learned that the mode is ideal for summarizing:
#   - Ordinal data represented using words.
#   - Nominal data.
#   - Discrete data (when the average value needs to be communicated to a non-technical audience).
# We also saw that the position of the mean, median, and mode is generally predictable for skewed and symmetrical distributions.
# Throughout the last three missions we learned how to measure the average value of a distribution. In the table below, you can see a summary of what we learned so far.