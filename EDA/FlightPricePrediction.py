import pandas as pd
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

df['Arrival_hour'] = df['Arrival_Time'].str.split(':').str[0]
df['Arrival_min'] = df['Arrival_Time'].str.split(':').str[1]
