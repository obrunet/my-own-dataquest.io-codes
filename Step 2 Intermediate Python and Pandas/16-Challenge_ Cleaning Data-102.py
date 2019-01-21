## 3. Exploring the Data ##

# The Avengers are a well-known and widely-loved team of superheroes  originally introduced in the 1960's. comic book series. The team at FiveThirtyEight has collected various data from different sites (see their write-up). There are still some inconsistencies.

# Clean up their data set so it can be more useful for analysis in pandas.

import pandas as pd

avengers = pd.read_csv("avengers.csv")

print(avengers.head(10))
avengers.shape
avengers.info()


## 4. Filtering Out Bad Data ##

# Because the data came from a crowdsourced community site, it could contain errors.


import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

# plot a histogram of the values in the Year column(when Marvel introduced each Avenger)
# notice some oddities. 
avengers['Year'].hist()

# keeps only the Avengers who were introduced after 1960
true_avengers = avengers[avengers['Year'] > 1959]

print(true_avengers.head(10))
true_avengers.info()

## 5. Consolidating Deaths ##

# total number of deaths each character experienced -> we'd like to have a single field containing that information.

deaths_columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
#true_avengers[deaths_columns]

def death_nb (row):
    nb = 0
    for death in deaths_columns:
        if row[death] == 'YES':
            nb += 1;
    return nb

true_avengers['Deaths'] = true_avengers.apply(lambda row: death_nb(row), axis=1)

## 6. Verifying Years Since Joining ##

# Final task: verify that the Years since joining field accurately reflects the Year column

joined_accuracy_count  = int()

# because this challenge was created in 2015, uses that year as reference
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]

# nb of accurate year = length of the panda serie:
joined_accuracy_count = len(correct_joined_years)

