import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from holoviews.plotting.bokeh.styles import font_size

df = pd.read_csv("..//CleanDataSets//google_cleaned.csv")
print(df.head())

print(df[df.duplicated('App')].shape)

## Observation -> DS has duplicate records
df = df.drop_duplicates(subset=['App'], keep='first')
print(df[df.duplicated('App')].shape)

numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

print('We have {} numerical : {}'.format(len(numeric_features), numeric_features))
print('\nWe have {} categorical : {}'.format(len(categorical_features), categorical_features))


## Proportion of count data on categorical columns
for col in categorical_features:
    print(df[col].value_counts(normalize=True)*100)

## Plot -> Numerical
plt.figure(figsize=(15,15))
plt.suptitle('Univariate Analysis of Numerical Features',fontsize=20,fontweight='bold',alpha=0.8,y=1)

for i in range(0,len(numeric_features)):
    plt.subplot(5,3,i+1)
    sns.kdeplot(x=df[numeric_features[i]],shade=True,color='r')
    plt.xlabel(numeric_features[i])
    plt.tight_layout()

plt.show()

## Observation -> Rating and Year are left skewed   and  Reviews,Size,Installs, Price are Right Skewed

## Plot -> Categorical
plt.figure(figsize=(15,15))
plt.suptitle('Univariate Analysis of Categorical Features',fontsize=20,fontweight='bold',alpha=0.8,y=1)
category=['Type','Content Rating']
for i in range(0,len(category)):
    plt.subplot(5,3,i+1)
    sns.countplot(x=df[category[i]],palette='Set2')
    plt.xlabel(numeric_features[i])
    plt.tight_layout()

plt.show()

### Which is the most Popular App Category

df['Category'].value_counts().plot.pie(y=df['Category'],figsize=(15,16))
plt.show()
## observation

### Top 10 app
category = df['Category'].value_counts().reset_index()
category.columns = ['Category', 'Count']

# Plot
plt.figure(figsize=(15,6))
sns.barplot(
    x='Category',
    y='Count',
    hue='Category',
    data=category[:10],
    palette='hls',
    legend=False
)

plt.title("Top 10 App Category")
plt.xticks(rotation=90)
plt.show()

### Which category has the largest number of installation
### What are the Top 5 most installed apps in each popular category
