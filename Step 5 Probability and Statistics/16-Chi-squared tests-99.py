## 2. Calculating differences ##

female_diff = (10771 - 16280.5) / 16280.5
# Compute the proportional difference in number of observed Females vs number of expected Females
male_diff = (21790 - 16280.5) / 16280.5

## 3. Updating the formula ##

# calculate the chi-squared value, by adding up all of the squared differences between observed and expected values.
female_diff = (10771 - 16280.5) **2 / 16280.5
male_diff = (21790 - 16280.5) **2 / 16280.5
gender_chisq = female_diff + male_diff

## 4. Generating a distribution ##

from numpy.random import random
import matplotlib.pyplot as plt

chi_squared_values = []

for i in range(1000):
    # Pass (32561,) into the numpy.random.random function to get a vector with 32561 elements
    sequence = random((32561,))                         # generate 32561 numbers between 0.0 and 1.0
    sequence[sequence < 0.5] = 0                
    sequence[sequence >= 0.5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    male_diff = (male_count - 16280.5) ** 2 / 16280.5
    female_diff = (female_count-16280.5)**2 / 16280.5
    chi = male_diff + female_diff
    chi_squared_values.append(chi)
    
plt.hist(chi_squared_values)

## 6. Smaller samples ##

female_diff = (107.71 - 162.805)**2 / 162.805
male_diff = (217.90 - 162.805)**2 / 162.805
gender_chisq = male_diff + female_diff

## 7. Sampling distribution equality ##

from numpy.random import random

chi_squared_values = []
for i in range(1000):
    sequence = random((300,))
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    male_diff = (male_count - 150)**2 / 150
    female_diff = (female_count - 150)**2 / 150
    chi = male_diff + female_diff
    chi_squared_values.append(chi)
    
plt.hist(chi_squared_values)

## 9. Increasing degrees of freedom ##

diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp) ** 2 / exp
    diffs.append(diff)
    
race_chisq = sum(diffs)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed=[27816,3124,1039,311,271]
expected=[26146.5,3939.9,944.3,260.5,1269.8]
# The scipy.stats.chisquare function takes in an array of observed frequences, and an array of expected frequencies, 
# and returns a tuple containing both the chi-squared value and the matching p-value 
# that we can use to check for statistical significance.
race_pvalue = chisquare(observed,expected)