## 1. Simplifying Data ##

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

wnba = pd.read_csv("wnba.csv")
wnba.shape
# print(wnba)
wnba.head()
# wnba.tail()

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()
print(freq_distro_pos)

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
# print(wnba['Height'].value_counts().sort_index())
age_ascending = wnba['Age'].value_counts().sort_index(ascending = True)
age_descending = wnba['Age'].value_counts().sort_index(ascending = False)

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)


# instead of 
# wnba['PTS_ordinal_scale'].value_counts()[['very few points', 'few points', ...]] -> use: 
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4, 3, 0, 2, 1, 5]]

## 5. Proportions and Percentages ##

# Because proportions and percentages are relative to the total number of instances in some set of data, they are called relative frequencies. In contrast, the frequencies we've been working with so far are called absolute frequencies because they are absolute counts and don't relate to the total number of instances.
wnba = pd.read_csv('wnba.csv')
percentages = wnba['Age'].value_counts(normalize = True).sort_index() * 100 # slightly faster than .value_counts() / len(wnba)
proportion_25 = percentages[25] / 100
percentage_30 = percentages[30]
percentage_over_30 = percentages.loc[30:].sum()
percentage_below_23 = percentages.loc[:23].sum()
# we can add .round(2) at the end

## 6. Percentiles and Percentile Ranks ##

wnba = pd.read_csv('wnba.csv')
from scipy.stats import percentileofscore
# use kind = 'weak' to indicate that we want to find the percentage of values that are =< than the value we specify in the score parameter
percentile_rank_half_less = percentileofscore(a = wnba['Games Played'], score = 34/2, kind = 'weak')
percentage_half_more = 100 - percentile_rank_half_less

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')
# print(wnba['Age'].describe())
# not interested in the first 3 rows: count, mean, and standard deviation -> print(wnba['Age'].describe().iloc[3:])
age_upper_quartile = wnba['Age'].describe().iloc[6]
age_middle_quartile = wnba['Age'].describe().iloc[5]
age_95th_percentile = wnba['Age'].describe(percentiles = [0.95]).iloc[5]
# percentiles for other percentages: wnba['Age'].describe(percentiles = [.1, .15, .33, .5, .592, .85, .9]).iloc[3:])

# A percentile is a value of a variable, and it corresponds to a certain percentile rank in the distribution of that variable. 
question1 = True
# A percentile rank is a numerical value from the distribution of a variable. 
question2 = False
# The 25th percentile is the same thing as the lower quartile, and the upper quartile is the same thing as the third quartile. 
question3 = True

## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
grouped_freq_table = wnba['PTS'].value_counts(bins = 10, normalize = True).sort_index(ascending = False) * 100

## 9. Information Loss ##

import pandas as pd
print(wnba['MIN'].value_counts(bins = 10).sort_index())

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')
# to increase readability and understanding, we can define the intervals ourselves
class_intervals = 10
intervals = pd.interval_range(start = 0, end = 600, freq = 600 / class_intervals)      # print(intervals) -> index
gr_freq_table_10 = pd.Series([0 for _ in range(class_intervals)], index = intervals)

for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table_10.loc[interval] += 1
            break
print(gr_freq_table_10)
print(gr_freq_table_10.sum())      # a quick sanity check