import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

df = pd.read_csv("..//DataSets//googleplaystore.csv")
print(df.head())
print(df.columns)
print(df.shape)  # (10841, 13)

print(df.isnull().sum())

# print(df['Reviews'].unique())
print(df[
          'Reviews'].str.isnumeric().sum())  # -> data in str but numeric ---> 10840 i.e. one is not in numeric (shape - (10841, 13)))

print(df[~df['Reviews'].str.isnumeric()])  # ~ is as not   ->  index = 10472

## Data Cleaning
df_copy = df.copy()
df_copy = df_copy.drop(df_copy.index[10472])

## convert review datatype to Int
df_copy['Reviews'] = df_copy['Reviews'].astype(int)

print(df_copy['Size'].unique())
df_copy['Size'] = df_copy['Size'].str.replace("M", "000")  # -> Million to Kilo
df_copy['Size'] = df_copy['Size'].str.replace("K", "")
df_copy['Size'] = df_copy['Size'].replace("Varies with device", np.nan)

print(df_copy['Installs'].unique())
print(df_copy['Price'].unique())

chars_to_remove = ['+', ',', '$']
cols_to_clean = ['Installs', 'Price']

for item in chars_to_remove:
    for col in cols_to_clean:
        df_copy[col] = df_copy[col].str.replace(item, "")

print(df_copy['Installs'].unique())
print(df_copy['Price'].unique())

df_copy['Installs'] = df_copy['Installs'].astype(int)
df_copy['Price'] = df_copy['Price'].astype(float)

## Handling Last Updated Feature
print(df_copy['Last Updated'].unique())
df_copy['Last Updated'] = pd.to_datetime(df_copy['Last Updated'])

df_copy['Day']=df_copy['Last Updated'].dt.day
df_copy['Month']=df_copy['Last Updated'].dt.month
df_copy['Year']=df_copy['Last Updated'].dt.year


df_copy.to_csv('..//CleanDataSets//google_cleaned.csv')