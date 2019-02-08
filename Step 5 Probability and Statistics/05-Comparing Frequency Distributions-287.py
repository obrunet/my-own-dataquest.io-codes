## 1. Comparing Frequency Distributions ##

rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']

rookie_distro = rookies['Pos'].value_counts()
little_xp_distro = little_xp['Pos'].value_counts()
experienced_distro = experienced['Pos'].value_counts()
very_xp_distro = very_xp['Pos'].value_counts()
veteran_distro = veterans['Pos'].value_counts()

## 2. Grouped Bar Plots ##

import seaborn as sns

sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba, order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'], hue_order = ['C', 'F', 'F/C', 'G', 'G/F'])

## 3. Challenge: Do Older Players Play Less? ##

sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative', data = wnba)
result='rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt
# plots only the shape of the histograms. We can do this using the histtype parameter and choose the 'step' type
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
# adds a vertical line to demarcate the average point
plt.axvline(x = 497, label = 'Average')
plt.legend()

## 5. Kernel Density Estimate Plots ##

# smooths out the shape of the histograms to make them look less dense on the graph
# kde to get a much clear picture about the shape of a distribution.
wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(x = 497, label = 'Average')
plt.legend()

## 7. Strip Plots ##

# examine the distribution of player weight (not height) as a function of player position :
sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
# bullet points overlap, so we can fix this by adding a bit of jitter to each distribution (set param to True)

## 8. Box plots ##

# The two lines extending upwards and downwards out of the box in the middle look a bit like two whiskers, reason for which we call this plot a box-and-whisker plot, or, more convenient, just box plot
sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)

## 9. Outliers ##

print(wnba['Games Played'].describe())
"""
0 count   143.000000 
1 mean    24.356643 
2 std     7.104259 
3 min     2.000000 
4 25%     22.000000 
5 50%     27.000000 
6 75%     29.000000 
7 max     32.000000
"""
upper_quartile = wnba['Games Played'].describe().iloc[6] 
lower_quartile = wnba['Games Played'].describe().iloc[4]
# interquartile range = 
iqr = upper_quartile - lower_quartile

# Using a factor of 1.5, calculate the lower and upper bound outside which values are considered outliers.
lower_bound = lower_quartile - iqr * 1.5
upper_bound = upper_quartile + iqr * 1.5

# how many values in the distribution are outliers_high
outliers_low = sum(wnba['Games Played'] < lower_bound)
outliers_high = sum(wnba['Games Played'] > upper_bound)

# plots a boxplot to check whether  answers are sensible
sns.boxplot(wnba['Games Played'])