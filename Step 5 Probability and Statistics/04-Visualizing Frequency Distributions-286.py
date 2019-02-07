## 2. Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()

## 3. Horizontal Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title = "Number of players in WNBA by level of experience")
# use rot = 45 to tilt the labels a bit at 45°:

## 4. Pie Charts ##

# The main advantage of pie charts over bar plots is that they provide a much better sense for the relative frequencies (proportions and percentages) in the distribution
wnba['Exp_ordinal'].value_counts().plot.pie()

## 5. Customizing a Pie Chart ##

import matplotlib.pyplot as plt
# percentages were automatically determined under the hood (don't need Series.value_counts(normalize = True) * 100)
# displayed using the autopct param
wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), autopct = '%.2f%%', title = "Percentage of players in WNBA by level of experience")
plt.ylabel('')  # removes title

## 6. Histograms ##

wnba['PTS'].plot.hist()

## 7. The Statistics Behind Histograms ##

# Under the hood, the wnba['PTS'].plot.hist() method:
#    - Generated a grouped frequency distribution table for the PTS variable with ten class intervals.
#    - For each class interval it plotted a bar with a height corresponding to the frequency of the interval.
from numpy import arange
wnba['Games Played'].describe()
wnba['Games Played'].plot.hist()
# wnba['PTS'].plot.hist(grid = True, xticks = arange(2,585,58.2), rot = 30)

## 9. Binning for Histograms ##

# The main difference is that in the case of a histogram there are no gaps between bars, and each bar represents an interval, not a single value.
wnba['Games Played'].plot.hist(range = (1,32), bins = 8, title = "The distribution of players by games played")
plt.xlabel('Games played')

## 10. Skewed Distributions ##

wnba['AST'].plot.hist() # blue
wnba['FT%'].plot.hist() # green
assists_distro = 'right skewed' # or positively skewed
ft_percent_distro = 'left skewed' # or negatively skewed

## 11. Symmetrical Distributions ##

# other 3 type: - symmetrical distribution - normal distribution (also called Gaussian distribution) - uniform distribution
wnba['Age'].plot.hist()             # blue
wnba['Height'].plot.hist()          # green
wnba['MIN'].plot.hist()             # red
normal_distribution = 'Height'