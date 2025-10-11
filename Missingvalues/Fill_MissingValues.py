import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('titanic')
print(df.head())

'''
Imputation Missing Values
'''
############################################################################

'''
# 1: Mean Value Imputation
Its help when data distributed normally
'''
print(sns.displot(df['age']))
plt.show()

df['age_mean']=df['age'].fillna(df['age'].mean())
print(df[['age_mean','age']])

#############################################################################

# if data is skewed
'''
# 2: Median Value Imputation
'''

df['age_median']=df['age'].fillna(df['age'].median())

#############################################################################

# if data is Categorical
'''
# 3: Mode Value Imputation
'''

print(df['embarked'].unique())
df['embarked_mode']=df['embarked'].fillna(df['embarked'].mode())
print(df[['embarked_mode','embarked']])
