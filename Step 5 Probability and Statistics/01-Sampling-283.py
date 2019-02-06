## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

wnba.head()
wnba.tail()
wnba.shape
parameter = wnba['Games Played'].max()
sample = wnba['Games Played'].sample(n=30, random_state=1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

parameter = wnba['PTS'].mean()  # mean
sample_means = []

for i in range (100):
    sample = wnba['PTS'].sample(n=10, random_state=i)
    sample_means.append(sample.mean())
    
plt.scatter(x=range(1,101),y=sample_means)
plt.axhline(parameter)

## 7. Stratified Sampling ##

# creates a new column which describes the number of points a player scored per game
wnba['points_per_game'] = wnba['PTS'] / wnba['Games Played']

position = wnba['Pos'].unique()
points_per_position = {}

# stratifies the wnba data set by player position, takes a sample & calculates mean
for pos in position:
    sample = wnba[wnba['Pos'] == pos].sample(n=10, random_state=0)
    points_per_position[pos] = sample['points_per_game'].mean()
  
# position with the greatest number of points per game
position_most_points = max(points_per_position, key = points_per_position.get)


## 8. Proportional Stratified Sampling ##

# the number of total points is influenced by the number of games played, which ranges from 2 to 32
print(wnba['Games Played'].min())
print(wnba['Games Played'].max())
# number intervals: (  indicates that the beginning of the interval is excluded, 
# ] indicates that the endpoint is included
print(wnba['Games Played'].value_counts(bins = 3, normalize = True) * 100)

# uses stratified sampling while being mindful of the proportions in the population
games_under_12 = wnba[wnba['Games Played'] <= 12]
games_btw_13_22 = wnba[(12 < wnba['Games Played']) & (wnba['Games Played'] <= 22)]
games_over_23 = wnba[22 < wnba['Games Played']]

pts_means = []
for i in range(100):
    sample_under_12 = games_under_12.sample(n=1, random_state=i) 
    sample_btw_13_22 = games_btw_13_22.sample(n=2, random_state=i)
    sample_over_23 = games_over_23.sample(n=7, random_state=i)
    all_samples = pd.concat([sample_under_12, sample_btw_13_22, sample_over_23])
    pts_means.append(all_samples['PTS'].mean())
    
plt.scatter(range(1,101), pts_means)
plt.axhline(wnba['PTS'].mean())

## 9. Choosing the Right Strata ##

print(wnba['MIN'].value_counts(bins = 10, normalize = True))

## 10. Cluster Sampling ##

# pick four team clusters randomly
random_team_clusters = pd.Series(wnba['Team'].unique()).sample(n=4, random_state=0)
new_df = pd.DataFrame()

# collects the data from each cluster without sampling the clusters
for team in random_team_clusters:
    new_df = new_df.append(wnba[wnba['Team'] == team])
    
sampling_error_height = wnba['Height'].mean() - new_df['Height'].mean()
sampling_error_age = wnba['Age'].mean() - new_df['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - new_df['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - new_df['PTS'].mean()