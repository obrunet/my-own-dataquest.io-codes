# My Dataquest Projects


This repository contains all my projects from the Dataquest.io website. 
These projects serve as reference notes for myself. There a lot of comments in order to show the process. 
At the end, besides the conclusion and the final analysis, there is a summary of what can be learnt and also further possible investigations.

### Step 01 - Project #1: Exploring US births (old course)
- Not done. Dataquest changed this course few week ago...

### Step 01 - Project #2: Exploring Gun Deaths in the US (old course)
- Files not saved and no backup :( Unfortunately Dataquest changed this course few week ago and i've lost the files. I'll do the new challenge in few weeks :]

### Step 02 - Project #1: [Exploring Ebay Car Sales Data](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2002.01%20Exploring%20Ebay%20Car%20Sales%20Data/Basics.ipynb)
- Goal: With a sample of 50,000 data points from the the full dataset of used car eBay Kleinanzeigen, the aim of this project is to clean the data and analyze the included used car listing
- Concepts explored: pandas, functions, boolean filtering
- Functions, methods, and properties used:  .read_csv(), .pivot_table(), .replace(), .describe(), .apply(), .isnull(), .columns, .shape, .head()

### Step 02 - Project #2: [Visualizing Earnings Based On College Majors](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2002.02%20Visualizing%20Earnings%20Based%20On%20College%20Majors/Basics.ipynb)
- Goal: With a dataset on the job outcomes of students who graduated from college between 2010 and 2012, the aim of this project is to analyse the data based on different plots.
- Concepts explored: pandas, matplotlib, histograms, bar charts, scatterplots, scatter matrices
- Functions, methods, and properties used:  .plot(), scatter_matrix(), hist(), iloc[], .head(), .tail(), .describe()

### Step 02 - Project #3: [Visualizing The Gender Gap In College Degrees](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2002.03%20Project_%20Visualizing%20The%20Gender%20Gap%20In%20College%20Degrees/Basics.ipynb)
- Goal: Generation of line charts to compare the gender gap across all degree categories. Export of the final diagram created as an image file.
- Concepts explored: pandas, matplotlib, histograms, line plots, chart graphics
- Functions, methods, and properties used:  .savefig(), .text(), .axhline(), .set_yticks(), .tick_params(), .set_title(), .set_ylim(), .set_xlim(), .spines(), .tick_params()

### Step 02 - Project #4: [Analyzing NYC High School Data](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2002.04%20Analyzing%20NYC%20High%20School%20Data/Schools.ipynb)
- Goal: NYC has a significant immigrant population and is very diverse, so comparing demographic factors such as race, income, and gender with SAT scores is a good way to determine whether the SAT is a fair test. In the last mission, I began performing some analysis. I'll extend that analysis.
- Concepts explored: pandas, matplotlib.pyplot, correlations, regex, basemap, data analysis, string manipulation
- Functions, methods, and properties used:  .scatter(), info(), .tolist(), .groupby(), .agg(), .concat(), .apply(), .strip, .merge(), .fillna(), .corr()

### Step 02 - Project #5: [Star Wars Survey](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2002.05%20Star%20Wars%20Survey/Basics.ipynb)
- Goal: The FiveThirtyEight team has surveyed Star Wars fans using the online tool SurveyMonkey and has collected data in order to answer questions like "does America realize that “The Empire Strikes Back” is clearly the best of the star wares movies?". In this project, I'm going to clean and explore this data set.
- Concepts explored: pandas, matplotlib.pyplot, data cleaning, string manipulation, bar plots
- Functions, methods, and properties used:  .read_csv(), .columns, notnull, map(), .dtypes, .rename, astype(), .mean(), .sum(), .xlabel(), .ylabel()

### Step 04 - Project #1: [Analyzing CIA Factbook](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2004.01%20Analyzing%20CIA%20Factbook%20Data%20Using%20SQLite%20and%20Python/Basics.ipynb)
- Goal: Based on the data from the CIA World Factbook, analysis of the population as of 2015, its growth rate, area of diffrerent countries, their density...
- Python/SQL concepts explored: python+sqlite3, pandas, SQL queries, SQL subqueries, matplotlib.plyplot, seaborn, histograms
- Functions, methods, and properties used: .cursor(), .read_sql_query(), .set_xlabel(), .set_xlim(), .add_subplot(), .figure()
- SQL statements used: SELECT, WHERE, FROM, MIN(), MAX(), ORDER BY, AND

### Step 04 - Project #2: [Answering Business Questions using SQL](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2004.02%20Answering%20Business%20Questions%20using%20SQL/Basics.ipynb) (not entirely finished...)
- Goal: With the Chinook database including the invoice of a platform selling music tracks and albums, analyse the top selling genres, the performances of employees, the sales by countries and the percentage of purchases for individual tracks vs whole albums.
- Python/SQL concepts explored: python+sqlite3, pandas, SQL queries, SQL subqueries, matplotlib.plyplot, pie charts
- Functions, methods, and properties used: pd.read_sql(,), conn.execute(), plot.bar() & plot.barh(), plot.pie()
- SQL statements used: SELECT, FROM, SUM(), INNER JOIN, GROUP BY, ORDER BY, WITH, CASE,  subqueries, multiple joins, set operations, aggregate functions and more

### Step 05 - Project #1: [Analyzing Fandango Movie Reviews](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2005.01%20Analyzing%20Fandango%20Movie%20Reviews/Basics.ipynb)
- Goal: Analysis of more recent movie ratings data to determine whether there are still lightly inflated and biaised.
- Python concepts explored: pandas, descriptive statistics, numpy, matplotlib, distributions using kernel density plots, plot bar, histogram
- Functions, methods, and properties used: .sort_values(), .hist(), .mean(), .median(), .mode(), .plot.kde(), .value_counts(), .plot.bar()

### Step 05.02 - Project #2: [Finding the Best Markets to Advertise In](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2005.02%20Finding%20the%20Best%20Markets%20to%20Advertise%20In/Basics.ipynb)
- Goal: Our e-learning company offers courses on web and mobile development but also covers many other domains, like data science. How to promote our products ? Find out the two best markets to advertise our product in.
- Python concepts explored: pandas, descriptive statistics, distributions, outliers removing, absolute and relative frequencies,
- Functions, methods, and properties used: .dropna(), .notnull(), .replace(), .sort_values(), .value_counts(), .mean(), .median().
                     
### Step 05.03 - Project #3: [Winning Jeopardy](https://github.com/obrunet/my-own-dataquest.io-codes/blob/master/Projects/Step%2005.03%20Winning%20Jeopardy/Basics.ipynb) (Results at the end are a little bit weird... I'll investigate this later...)
- Goal: Jeopardy is a popular TV show in the US where participants answer questions to win money. Let's say we want to compete on Jeopardy. Figure out if there are some patterns in the questions that could help.
- Python concepts explored: scipy.stats, descriptive statistics, normalizing text and values, chi-squared
- Functions, methods, and properties used: .chisquare(), regex .mean(), .iterrows(), .apply().
