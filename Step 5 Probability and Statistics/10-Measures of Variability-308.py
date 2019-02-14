## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def get_range(val_array):
    # takes in an array of numerical values and returns the range of that array
    return (max(val_array) - min(val_array))

range_by_year = {}
years = houses['Yr Sold'].unique()
for y in years:
    range_by_year[y] = get_range(houses[houses['Yr Sold'] == y]['SalePrice'])

two = True
one = False

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def get_avg_dist(val_array):
    # takes in a numerical array and returns the average distances
    distances = []
    mean = sum(val_array)/len(val_array)
    for val in val_array:
        distances.append(mean - val)
    return( sum(distances)/len(distances), mean)

avg_distance, mean = get_avg_dist(C)
print(avg_distance) # we got a value of 0 because the mean is the balance point of a distribution

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]
# let's take the absolute value (also called modulus) of each distance, and sum them up
# the distance of a value from the mean is called deviation

def mean_abs_dev(num_array):
    # calculates the mean absolute deviation (or average absolute deviation) of an array
    mean = sum(num_array)/len(num_array)
    abs_distances = []
    for num in num_array:
        abs_distances.append(abs(mean - num))
    return sum(abs_distances)/len(abs_distances)

mad = mean_abs_dev(C)
# the result is considerably less than 20 but greater than 0, as expected

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]
# mean squared distance or mean squared deviation commonly known as variance
def get_variance(num_array):
    # takes in a numerical array and returns the variance of that array
    mean = sum(num_array)/len(num_array)
    squared_dist = []
    for num in num_array:
        squared_dist.append((mean - num)**2)
    return sum(squared_dist)/len(squared_dist)

variance_C = get_variance(C)    

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]
# drawback = squares the units of measurement
# The square root of variance is called standard deviation (remember that "deviation" is synonymous with "distance")

def get_std_dev(num_array):
    # takes in a numerical array and returns the standard deviation of that array
    mean = sum(num_array)/len(num_array)
    squared_dist = []
    for num in num_array:
        squared_dist.append((mean - num)**2)
    return sqrt(sum(squared_dist)/len(squared_dist))

standard_deviation_C = get_std_dev(C)    
# the result is considerably less than 20 but greater than 0

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    return sqrt(variance)

# mean = houses['SalePrice'].mean()
# st_dev = standard_deviation(houses['SalePrice'])
# houses['SalePrice'].plot.hist()
# plt.axvline(mean, color = 'Black', label = 'Mean')
# plt.axvline(mean - st_dev, color = 'Red', label = 'Below')
# plt.axvline(mean + st_dev, color = 'Violet', label = 'Above')
# plt.legend()

years = {}
for y in houses['Yr Sold'].unique():
    year_segment = houses[houses['Yr Sold'] == y]
    st_dev = standard_deviation(year_segment['SalePrice'])
    years[y] = st_dev

greatest_variability = max(years, key = years.get)
lowest_variability = min(years, key = years.get)

## 7. A Measure of Spread ##

# Another way to understand standard deviation is as a measure of spread in a distribution
sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    variance = sum(distances) / len(distances)
    return sqrt(variance)

bigger_spread = 'sample 2'
st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)


## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    variance = sum(distances) / len(distances)
    return sqrt(variance)

import matplotlib.pyplot as plt

st_devs = []
for i in range (5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_devs.append(standard_deviation(sample))
    
plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))


## 9. Bessel's Correction ##

# the sample standard deviation underestimates on average the population standard deviation
def standard_deviation_bessel(array):
    reference_point = sum(array) / len(array)
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    # small correction added to the sample standard deviation (dividing by n-1 instead of n) is called Bessel's correction.
    variance = sum(distances) / (len(distances)-1)
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation_bessel(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std(ddof = 1)
numpy_stdev = sample['SalePrice'].std(ddof = 1)
equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var(ddof = 1)
numpy_var = var(sample['SalePrice'],ddof = 1)
equal_vars = pandas_var == numpy_var 

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)

st_devs = []
variances = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))
    
mean_std = sum(st_devs) / len(st_devs)
mean_var = sum(variances) / len(variances)

equal_stdev = pop_std == mean_std
equal_var = pop_var == mean_var



# we learned how to measure the variability of a distribution using the range, the mean absolute deviation, the variance, and the standard deviation. 
# These metrics are ideal for measuring the variability of distributions whose values are measured on an interval or ratio scale.
# Measuring variability for ordinal and nominal data is much harder because we can't quantify the differences between values. 
# For this reason, little is written in the literature about measuring variability for ordinal and nominal data. 
# If you want to dig more into this, you can start by reading this paper.