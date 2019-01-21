## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

ap_2010_df = pd.read_csv("schools/ap_2010.csv")
class_size_df = pd.read_csv("schools/class_size.csv")
demographics_df = pd.read_csv("schools/demographics.csv")
graduation_df = pd.read_csv("schools/graduation.csv")
hs_directory_df = pd.read_csv("schools/hs_directory.csv")
sat_results_df = pd.read_csv("schools/sat_results.csv")

data['ap_2010'] = ap_2010_df
data['class_size'] = class_size_df
data['demographics'] = demographics_df
data['graduation'] = graduation_df
data['hs_directory'] = hs_directory_df
data['sat_results'] = sat_results_df 

## 5. Exploring the SAT Data ##

print(data['sat_results'].head())

## 6. Exploring the Remaining Data ##

for elt in data:
    print(data[elt].head())

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')

# After we read in the survey data, we'll want to combine it into a single dataframe. We can do this by calling the pandas.concat() function:
# z = pd.concat([x,y], axis=0)
# The code above will combine dataframes x and y by essentially appending y to the end of x. The combined dataframe z will have the number of rows in x plus the number of rows in y

survey = pd.concat([all_survey, d75_survey], axis=0)
survey.head()

## 9. Cleaning Up the Surveys ##

survey['DBN'] = survey['dbn']
survey = survey[["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]]
data['survey'] = survey
data['survey'].info()

## 11. Inserting DBN Fields ##

data['hs_directory']['DBN'] = data['hs_directory']['dbn']

# Converts the input  number to a string - Check it's length 
# If two digits long, returns the string. If one digit long, adds a 0 to the front, then returns it.
def custom_func(nb):
    string = str(nb)
    if len(string) == 2:
        return string
    elif len(string) == 1:
        return string.zfill(2)
    else:
        print("problem...there is a string stricly longer than 2 letters...") 

# Create a new column called padded_csd in the class_size data set by using the pandas.Series.apply() method 
data['class_size']['padded_csd'] = data["class_size"]["CSD"].apply(custom_func) 

# Use the addition operator (+) along with the padded_csd and SCHOOL CODE columns of class_size, then assign the result to the DBN column of class_size.
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']

# Display the first few rows of class_size to double check the DBN column.
data['class_size'].head()

## 12. Combining the SAT Scores ##

data['sat_results']['SAT Math Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Math Avg. Score'], errors="coerce")
data['sat_results']['SAT Critical Reading Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Critical Reading Avg. Score'], errors="coerce")
data['sat_results']['SAT Writing Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Writing Avg. Score'], errors="coerce")
                    
data['sat_results']['sat_score'] = data['sat_results']['SAT Math Avg. Score'] + data['sat_results']['SAT Critical Reading Avg. Score'] + data['sat_results']['SAT Writing Avg. Score']

data['sat_results']['sat_score'].head()

## 13. Parsing Geographic Coordinates for Schools ##

import re

# Takes in a string - extracts the coordinates - pull out and returns the latitude
def lat_extraction(st):
    coords = re.findall("\(.+\)", st)   # will return [(latitude float, longitude float)]
    result = coords[0].split(',')[0].replace('(', '')
    return result

data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(lat_extraction)
data['hs_directory'].head()

## 14. Extracting the Longitude ##

import re

# Takes in a string - extracts the coordinates - pull out and returns the longitude
def lon_extraction(st):
    coords = re.findall("\(.+\)", st)   # will return [(latitude float, longitude float)]
    result = coords[0].split(',')[1].replace(')', '')
    return result

data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(lon_extraction)

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')

data['hs_directory'].head()