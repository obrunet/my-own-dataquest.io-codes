## 3. Condensing the Class Size Data Set ##

class_size = data['class_size']
class_size = class_size[class_size['GRADE ']=='09-12']
class_size = class_size[class_size['PROGRAM TYPE']=='GEN ED']
class_size.head()
                         

## 5. Computing Average Class Sizes ##

import numpy

class_size = class_size.groupby('DBN').agg(numpy.mean)

class_size.reset_index(inplace=True)
data['class_size'] = class_size
print(data['class_size'].head())

## 7. Condensing the Demographics Data Set ##

demographics = data['demographics']
demographics = demographics[demographics['schoolyear'] == 20112012]
data['demographics'] = demographics
data['demographics'].head()

## 9. Condensing the Graduation Data Set ##

graduation = data['graduation']
graduation = graduation[graduation['Cohort'] == '2006']
graduation = graduation[graduation['Demographic'] == 'Total Cohort']

data['graduation'] = graduation
data['graduation'].head()

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for c in cols:
    data['ap_2010'][c] = pd.to_numeric(data['ap_2010'][c], errors="coerce")

print(data['ap_2010'].dtypes)

## 12. Performing the Left Joins ##

combined = data['sat_results']

combined = combined.merge(data['ap_2010'], on='DBN', how='left')
combined = combined.merge(data['graduation'], on='DBN', how='left')
combined.head()
combined.shape

## 13. Performing the Inner Joins ##

# Now that we've performed the left joins, we still have to merge class_size, demographics, survey, and hs_directory into combined. Because these files contain information that's more valuable to our analysis and also have fewer missing DBN values, we'll use the inner join type.


list_to_merge = ['class_size', 'demographics', 'survey', 'hs_directory']

for df in list_to_merge:
    combined = combined.merge(data[df], on='DBN', how='inner')

combined.head()
combined.shape

## 15. Filling in Missing Values ##

# Calculate the means of all of the columns in combined using the pandas.DataFrame.mean() method.
means = combined.mean()

# Fill in any missing values in combined with the means of the respective columns using the pandas.DataFrame.fillna() method.
combined = combined.fillna(means)

# Fill in any remaining missing values in combined with 0 using the df.fillna() method.
combined = combined.fillna(0)

# Display the first few rows of combined to verify that the correct operations occurred.
combined.head()

## 16. Adding a School District Column for Mapping ##

# extracts the first two characters of a string and returns them
def first_two_char(st):
    return st[0:2]

combined['school_dist'] = combined['DBN'].apply(first_two_char)
combined.head()