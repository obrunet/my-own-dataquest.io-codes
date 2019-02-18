## 2. Calculating expected values ##

males_over50k = .67 * .241 * 32561
males_under50k = .67 * .759 * 32561
females_over50k = .33 * .241 * 32561
females_under50k = .33 * .759 * 32561

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)

## 4. Finding statistical significance ##

from scipy.stats import chisquare
expected = [5249.8, 2597.4, 16533.5, 8180.3]
observed = [6662, 1179, 15128, 9592]
pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas
table = pandas.crosstab(income["sex"], [income["race"]])
# The above code will print a table showing how many people from income fall into each category of sex and race.
print(table)

## 6. Finding expected values ##

import pandas
from scipy.stats import chi2_contingency

table = pandas.crosstab(income["sex"], [income["race"]]) 
# the scipy.stats.chi2_contingency function  takes in a cross table of observed counts, and returns 
# the chi-squared value, the p-value, the degrees of freedom, and the expected frequencies
chisq_value, pvalue_gender_race, df,expected = chi2_contingency(table)



# Now that we've learned the chi-squared test, you should be able to figure out if the association between two columns of categorical data is statistically significant or not. There are a few caveats to using the chi-squared test that are important to cover, though:
# Finding that a result isn't significant doesn't mean that no association between the columns exists. For instance, if we found that the chi-squared test between the sex and race columns returned a p-value of .1, it wouldn't mean that there is no relationship between sex and race. It just means that there isn't a statistically significant relationship.
# Finding a statistically significant result doesn't imply anything about what the correlation is. For instance, finding that a chi-squared test between sex and race results in a p-value of .01 doesn't mean that the dataset contains too many Females who are White (or too few). A statistically significant finding means that some evidence of a relationship between the variables exists, but needs to be investigated further.
# Chi-squared tests can only be applied in the case where each possibility within a category is independent. For instance, the Census counts individuals as either Male or Female, not both.
# Chi-squared tests are more valid when the numbers in each cell of the cross table are larger. So if each number is 100, great -- if each number is 1, you may need to gather more data.