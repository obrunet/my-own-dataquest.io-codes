## 1. Introduction ##

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])

## 2. Frequency Distribution ##

fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts().sort_index()
imdb_distribution = norm_reviews['IMDB_norm'].value_counts().sort_index()
print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig, ax = plt.subplots()

ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0, 5))
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))

ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'], bins=20, range=(0, 5))
ax2.hist(norm_reviews['RT_user_norm'], bins=20, range=(0, 5))
ax3.hist(norm_reviews['Metacritic_user_nom'], bins=20, range=(0, 5))
ax4.hist(norm_reviews['IMDB_norm'], bins=20, range=(0, 5))

ax1.set_title('Distribution of Fandango Ratings')
ax2.set_title('Distribution of Rotten Tomatoes Ratings')
ax3.set_title('Distribution of Metacritic Ratings')
ax4.set_title('Distribution of IMDB Ratings')

ax1.set_ylim(0, 50)
ax2.set_ylim(0, 50)
ax3.set_ylim(0, 50)
ax4.set_ylim(0, 50)

plt.show()

## 7. Box Plot ##

fig, ax = plt.subplots()

ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_ylim(0, 5)
ax.set_xticklabels(['Rotten Tomatoes'])

plt.show()

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

#Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
fig, ax = plt.subplots()

#Generate a box plot containing a box-and-whisker diagram for each column in num_cols.
ax.boxplot(norm_reviews[num_cols].values)

#Set the x-axis tick labels to the column names in num_cols and rotate the ticks by 90 degrees.
ax.set_xticklabels(norm_reviews[num_cols], rotation=90)

#Set the y-axis limit to range from 0 to 5.
ax.set_ylim(0, 5)

plt.show()