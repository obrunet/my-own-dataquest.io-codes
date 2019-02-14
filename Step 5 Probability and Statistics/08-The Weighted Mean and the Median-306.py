## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']
sums = houses_per_year['sum_per_year'].sum()
weighted_mean = sums / houses_per_year['Houses Sold'].sum()
mean_original = houses['SalePrice'].mean()
difference = round(mean_original, 10) - round(weighted_mean, 10)

## 3. The Weighted Mean ##

from numpy import average

def weighted_mean(means,weights):
    weighted_sum = []
    for mean, weight in zip(means, weights):
        weighted_sum.append(mean * weight)
    return sum(weighted_sum) / sum(weights)

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])
weighted_mean_numpy = numpy.average(houses_per_year['Mean Price'], weights = houses_per_year['Houses Sold'])
equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

# Sort the values
ta = houses['TotRms AbvGrd'].copy()
ta = ta.replace('10 or more', 10)
ta = ta.astype(int)
ta = ta.sort_values()
# Find the median
middle_indices = [int((len(ta) / 2)), int((len(ta) / 2 + 1))]
middle_values = ta.iloc[middle_indices] # make sure you don't use loc[]
median = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

# visualize the distributions using a box plot, outliers will appear as dots on the graph.
houses['Lot Area'].plot.box()
houses['SalePrice'].plot.box()

# compute the median and the mean
la_mean = houses['Lot Area'].mean()
la_median = houses['Lot Area'].median()
lotarea_difference = la_mean - la_median

sp_mean = houses['SalePrice'].mean()
sp_median = houses['SalePrice'].median()
saleprice_difference = sp_mean - sp_median

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()
houses['Overall Cond'].plot.hist()
more_representative = 'mean'