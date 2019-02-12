## 2. The Mean ##

import numpy as np

distribution = [0,2,3,3,3,4,13]
mean = np.mean(distribution)

if mean == (0+13)/2: # is the mean at the center ofthe distribution's range ?
    center = True
else:
    center = False
    
# Check whether the sum of the distances of the values that are below the mean is equal to the sum of the distances of the values that are above the mean
sum_distance_below, sum_distance_above = 0, 0
for i in distribution:
    if i < mean:
        sum_distance_below += (i-mean)
    elif i > mean:
        sum_distance_above += (mean-i)
if sum_distance_above == sum_distance_below:
    equal_distances = True
else:
    equal_distances = False

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
equal_distances = 0

for i in range(5000):
    seed(i)
    distribution = randint(0,1000,10)
    mean = sum(distribution) / len(distribution)
    
    above = []
    below = []
    for value in distribution:
        if value == mean:
            continue # continue with the next iteration because the distance is 0
        if value < mean:
            below.append(mean - value)
        if value > mean:
            above.append(value - mean)
    
    sum_above = round(sum(above),1)
    sum_below = round(sum(below),1)
    if (sum_above == sum_below):
        equal_distances += 1
# At the end equal_distances should have a value of 5000

## 4. Defining the Mean Algebraically ##

# We use the symbol "mew" to denote the population mean of N values
one = False
# If a population has 8 values, then N = 8 not n
two = False
# "x-bar" is used to denote the sample mean of n values
three = False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

# We can use sum() to compute the sum of an array without using a for loop, but for learning purposes
def sigma(nb_array):
    sum, l = 0, len(nb_array)
    # returns the mean value of the array of nb_
    for i in range(l):
        sum += nb_array[i-1]
    return (sum / l)

mean_1 = sigma(distribution_1)
mean_2 = sigma(distribution_2)
mean_3 = sigma(distribution_3)

## 6. Introducing the Data ##

import pandas as pd
# Use the pd.read_table() function or pd.read_csv(sep = '\t') to read in the data set.
houses = pd.read_table("AmesHousing_1.txt")
houses.head()
# This data set has variables measured on every scale of measurement: nominal, ordinal, interval and ratio.
one = True
# The SalePrice column is continuous and measured on an interval scale
two = False
#  If we wanted to measure the mean sale prices for all the houses sold between 2006 and 2010 in Ames, Iowa, the data stored in the AmesHousing_1.txt would be a sample. 
three = True

## 7. Mean House Prices ##

houses['SalePrice'].describe() # the distribution has a large range

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value 
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])
pandas_mean = houses['SalePrice'].mean()
if function_mean == pandas_mean:
    means_are_equal = True
else:
    means_are_equal = False

## 8. Estimating the Population Mean ##

# Our aim is to reduce the sampling error mew - x-bar. 2 factors that influence the sampling error are:
# - Sample representativity — the more representative a sample is, the closer  will be to .
# - Sample size — the larger the sample, the more chances we have to get a representative sample.
mean = houses['SalePrice'].mean()
sample_size = 5
sample_sizes, sampling_errors = [], []
for i in range(101):
    sample = houses['SalePrice'].sample(sample_size, random_state = i)
    sampling_errors.append(mean - sample.mean())
    sample_sizes.append(sample_size)
    sample_size += 29

# Generates a scatter plot to represent visually how the sampling error changes as the sample size increases
import matplotlib.pyplot as plt
plt.scatter(sample_sizes, sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')

## 9. Estimates from Low-Sized Samples ##

sample_size = 100
means = []
for i in range(10000):
    sample = houses['SalePrice'].sample(sample_size, random_state = i)
    means.append(sample.mean())

# generates a histogram to visualize the distribution of sample means
import matplotlib.pyplot as plt
plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel("Sample mean")
plt.ylabel("Frequency")
plt.xlim(0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
# Checks whether the population mean of the population [3, 7, 2] is equal to the mean of all the sample means of size 2 that we can get if we do sampling without replacement
samples = [[3, 7], [3, 2],
           [7, 2], [7, 3],
           [2, 3], [2, 7]
          ]
# Computes the mean of all the sample means
sample_means = []
for sample in samples:
    sample_means.append(sum(sample) / len(sample))
    
population_mean = sum(population) / len(population)
mean_of_sample_means = sum(sample_means) / len(sample_means)

unbiased = (population_mean == mean_of_sample_means)