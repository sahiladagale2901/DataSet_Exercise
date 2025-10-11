"""
 If we have 1000 points of dataset
 
 Yes -> 900
 No -> 100
 ration is 9:1
 
 then the model is biased towards Yes
 -> Called Imbalanced dataset
"""

# 1: Up Sampling

import numpy as np
import pandas as pd

# Set the random seed for reproducibility
np.random.seed(123)

# Create a dataframe with two classes
n_sample = 1000
class_0_ratio = 0.9
n_class_0 = int(n_sample * class_0_ratio)
n_class_1 = n_sample - n_class_0

## Create my dataframe with imbalanced dataset
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

df = pd.concat([class_0, class_1]).reset_index(drop=True)

print(df.head())

print(df['target'].value_counts())

######################################################################################################################
'''Up Sampling'''
df_majority = df[df['target'] == 0]
df_minority = df[df['target'] == 1]

from sklearn.utils import resample

df_minority_upsampled = resample(df_minority, replace=True,
                                 n_samples=len(df_majority),
                                 random_state=42)
print(df_minority_upsampled.shape)

df_upsampled = pd.concat([df_majority, df_minority_upsampled])
print(df_upsampled.head())

print(df_upsampled['target'].value_counts())

######################################################################################################################
# Set the random seed for reproducibility
np.random.seed(123)

# Create a dataframe with two classes
n_sample = 1000
class_0_ratio = 0.9
n_class_0 = int(n_sample * class_0_ratio)
n_class_1 = n_sample - n_class_0


## Create my dataframe with imbalanced dataset
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

df = pd.concat([class_0, class_1]).reset_index(drop=True)
'''Down Sampling'''
df_majority = df[df['target'] == 0]
df_minority = df[df['target'] == 1]

df_majority_upsampled = resample(df_minority, replace=False,
                                 n_samples=len(df_minority),
                                 random_state=42)
print(df_majority_upsampled.shape)

df_downsampled = pd.concat([df_minority, df_majority_upsampled])
print(df_downsampled.head())

print(df_downsampled['target'].value_counts())
