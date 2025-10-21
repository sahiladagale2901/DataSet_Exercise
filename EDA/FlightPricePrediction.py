import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('..//DataSets//Data_Train.xlsx')
print(df.head())

print(df.info())

## Feature Engineering
df['Date'] = df['Date_of_Journey'].str.split('/').str[0]
df['Month'] = df['Date_of_Journey'].str.split('/').str[1]
df['Year'] = df['Date_of_Journey'].str.split('/').str[2]

## Change to Int
df['Date'].astype(int)
df['Month'].astype(int)
df['Year'].astype(int)

df.drop('Date_of_Journey', axis=1, inplace=True)

df['Arrival_Time'] = df['Arrival_Time'].apply(lambda x: x.split(" ")[0])
df['Arrival_hour'] = df['Arrival_Time'].str.split(':').str[0].astype(int)
df['Arrival_min'] = df['Arrival_Time'].str.split(':').str[1].astype(int)
df.drop('Arrival_Time', axis=1, inplace=True)

df['Dep_hour'] = df['Dep_Time'].str.split(':').str[0].astype(int)
df['Dep_min'] = df['Dep_Time'].str.split(':').str[1].astype(int)
df.drop('Dep_Time', axis=1, inplace=True)

# print(df[['Dep_Time','Dep_hour','Dep_min']])

print(df['Total_Stops'].unique())
print(df['Total_Stops'].isnull().sum())

# mapping values with integer
df['Total_Stops'] = df['Total_Stops'].map(
    {'non-stop': 0, '2 stops': 2, '1 stop': 1, '3 stops': 3, '4 stops': 4, np.nan: 1})

print(df['Total_Stops'].isnull().sum())

# we have src and dest already
df.drop('Route', axis=1, inplace=True)

df['Duration_hour'] = df['Duration'].str.split(' ').str[0].str.split('h').str[0].astype(int)
df['Duration_min'] = df['Duration'].str.split(' ').str[1].str.split('m').str[0].astype(int)

print(df['Source'].unique())
print(df['Additional_Info'].unique())
print(df['Airline'].unique())

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
pd.DataFrame(encoder.fit_transform(df[['Source', 'Additional_Info', 'Airline']]).toarry(),
             columns=encoder.get_feature_names_out())

print(df)