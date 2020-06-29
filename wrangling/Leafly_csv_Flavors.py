# Leafly_csv_Flavors.py

# Wrangle to get unique flavors for front end user survey and ML use
 
# Second wrangle to strip "[]"" from list of Flavor in Flavor column values
# and replace "," with " " in attempt for better neural networking fit.



# Imports

from os import path
import pandas as pd


# Import Leafly csv

file_name = path.join(path.dirname(__file__), "../data/Leafly.csv")

df = pd.read_csv(file_name)

df = df.dropna()


# Examine the Leafly csv data head

#print(df.head())


# First wrangle for unique flavor

# Check type of Flavor column data

print(type(df.Flavor[1])) # <class 'str'>


# Strip and split the Flavor column string data in order to get unique values

df.Flavor.str.strip('[]').str.split(',')

stripped_flavor = list(set([a for b in df.Flavor.str.strip('[]').str.split(',') for a in b]))

# Verify the Flavor column data had changed from string to set to list

print(type(stripped_flavor))


# Function to get unique values 

def unique(flavor): 
      
    # Insert the list to the set 

    flavor_set = set(stripped_flavor) 

    # Convert the set to the list 

    unique_list_of_flavor = (list(flavor_set)) 
    for x in unique_list_of_flavor: 
        print(x)

# Commented out as job is done, and on to second wrangle

print(unique(stripped_flavor))

# 47 Unique Flavors

# Plum
# Chestnut
# Earthy
# Apricot
# Sage
# Skunk
# Berry
# Strawberry
# Blue
# Tropical
# Blueberry
# Honey
# Coffee
# Tea
# Vanilla
# Peach
# Fruit
# Lime
# Menthol
# Tobacco
# Mint
# Cheese
# Lavender
# Grape
# Chemical
# Minty
# Pepper
# Ammonia
# Grapefruit
# Citrus
# Violet
# Pear
# Mango
# Diesel
# Lemon
# Nutty
# Spicy/Herbal
# Butter
# Woody
# Pine
# Apple
# Flowery
# Tar
# Sweet
# Orange
# Rose
# Pungent
# Pineapple
# Tree


## Second wrangle
#
## Make the stripped, split and replace in Flavor column persist (uses strip and split from Wrangle 1)
#
#df["Flavor"] = df["Flavor"].str.replace(","," ").astype(str)
#
## Check type after strip and split, which is <class 'pandas.core.series.Series'>
#
#print(type(df['Flavor']))
#
## Verify changes with printout to terminal
#
#print(df['Flavor'].head())
#
## Set pandas option to show all columns in final printout verification
#
#pd.set_option('display.max_columns', None)
#
#print(df.head())
#
## Export csv for testing in neural network baseline
#
#file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly_nolistcommas.csv"
#
#df.to_csv(file_name, sep='\t', encoding='utf-8')
