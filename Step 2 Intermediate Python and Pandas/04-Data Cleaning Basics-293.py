## 1. Reading CSV Files with Encodings ##

import pandas as pd
laptops_df = pd.read_csv('laptops.csv', encoding='Latin-1')
laptops_df.info()

## 2. Cleaning Column Names ##

def clean_col(col):
    col = col.strip()
    col = col.replace("Operating System", "os")
    col = col.replace(" ", "_")
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.lower()
    return(col)

laptops.columns = [clean_col(c) for c in laptops.columns]
print(laptops.columns)

## 3. Converting String Columns to Numeric ##

laptops["screen_size"] = laptops["screen_size"].str.replace('"','').astype(float)
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)

laptops["ram"] = laptops["ram"].str.replace("GB", "").astype(int)
laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)

dtypes = laptops.dtypes

## 4. Practicing Converting String Columns to Numeric ##

laptops["weight"] = (laptops["weight"]
                     .str.replace("kgs", "")
                     .str.replace("kg", "")
                     .str.replace("[a-zA-Z]", "")
                     .astype(float)
                    )
laptops.rename({"weight": "weight_kg"}, axis=1, inplace=True)

laptops["price_euros"] = laptops["price_euros"].str.replace(",", ".").astype(float)
                     

weight_describe = laptops["weight_kg"].describe()
price_describe = laptops["price_euros"].describe()
    

## 5. Extracting Values from the Start of Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_manufacturer"] = (laptops["cpu"]
                  .str.split(n=1, expand=True)
                  .iloc[:,0]
                 )

## 6. Extracting Values from the End of Strings ##

screen_res = laptops["screen"].str.rsplit(n=1, expand=True)
screen_res.columns = ["A", "B"]
screen_res.loc[screen_res["B"].isnull(), "B"] = screen_res["A"]
laptops["screen_resolution"] = screen_res["B"]


laptops['cpu_speed_ghz'] = (laptops['cpu']
                            .str.replace('GHz', '')
                            .str.rsplit(n=1, expand=True)
                            .iloc[:,1]
                            .astype(float)
                           )

## 7. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
laptops['os'] = laptops['os'].map(mapping_dict)

## 8. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna()         # by default axis=0
laptops_no_null_cols = laptops.dropna(axis=1)

## 9. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

laptops.loc[laptops['os'] == 'No OS', 'os_version'] = 'Version Unknown'
value_counts_after = laptops.loc[laptops['os_version'].isnull(), 'os'].value_counts()

## 10. Challenge: Extracting Storage Information ##

# Clean the storage columns in common of the 2 disks
laptops['storage'] = (laptops['storage']
                      .str.replace('TB', '000')
                      .str.replace('GB', '')                    
                     )

# Split the columns
storage = laptops['storage'].str.split('+', n=1, expand=True)
storage.columns = ["disk_1", "disk_2"]


# Differentiate capacity and type for each disk 
storage_1 = storage["disk_1"].str.split(n=1, expand=True)
storage_2 = storage["disk_2"].str.rsplit(n=1, expand=True)
storage_1.columns, storage_2.columns = ["capacity", "type"], ["capacity", "type"]

# check if the split works well :)
#print(storage_1.loc[76:81, :])
#print(storage_2.loc[76:81, :])


# Clean the columns for both disks & add columns to laptops
# 2nd disk: no need to fill the none value with '0' string or Nan
laptops['storage_1_capacity_gb'] = storage_1['capacity'].str.strip().astype(float)
laptops['storage_1_type'] = storage_1['type'].str.strip()                                   

laptops['storage_2_capacity_gb'] = storage_2['capacity'].str.strip().astype(float)
laptops['storage_2_type'] = storage_2['type'].str.strip()        


# Drop the original storage column and temporary columns
laptops = laptops.drop('storage', axis=1)

## 11. Reordering Columns and Exporting Cleaned Data ##

laptops_dtypes = laptops.dtypes
cols = ['manufacturer', 'model_name', 'category', 'screen_size_inches',
        'screen', 'cpu', 'cpu_manufacturer', 'screen_resolution', 'cpu_speed_ghz', 'ram_gb',
        'storage_1_type', 'storage_1_capacity_gb', 'storage_2_type',
        'storage_2_capacity_gb', 'gpu', 'gpu_manufacturer', 'os',
        'os_version', 'weight_kg', 'price_euros']

laptops = laptops[cols]

laptops.to_csv('laptops_cleaned.csv', index=False)

laptops_cleaned = pd.read_csv('laptops_cleaned.csv')
laptops_cleaned_dtypes = laptops_cleaned.dtypes
