import pandas as pd
from IPython.core.pylabtools import figsize

df = pd.read_csv("..//DataSets//winequality-red.csv")
print(df.head())

## Summary
print(df.info())

## min, max, std, 25%,.. etc
# print(df.describe())

## shape
print(df.shape)

## List of all the columns
print(df.columns)

## Unique values of specific column
print(df['quality'].unique())

## Missing values in Dataset
print(df.isnull().sum())

## Find the Duplicate records
print(df.duplicated())  # -> True / False
print(df[df.duplicated()])  # -> provide data of True values

## Remove the Duplicates
df.drop_duplicates(inplace=True)
print(df[df.duplicated()])

## Co-relation
import seaborn as sns
import matplotlib.pyplot as plt

# Compute correlation matrix
# corr = df.corr()
# Set the figure size BEFORE plotting
plt.figure(figsize=(10, 10))
# Create heatmap
sns.heatmap(df.corr(), annot=True)
# Display the plot
plt.show()
