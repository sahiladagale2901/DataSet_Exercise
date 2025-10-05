'''
SMOTE-> Synthetic Minority Oversampling Technique

    usd to address imbalanced datasets where the minority class has significantly fewer instances then the majority class.
    its involves generating synthetic instances of minority class by interpolating b/w existing instances.
'''

from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000,
                           n_features=2,  # 2 feature
                           n_clusters_per_class=1,  # one cluster with 2 feature
                           weights=[.90],  # weight of 1 feature is 90%
                           n_redundant=0,
                           random_state=12)

import pandas as pd

df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])

df = pd.concat([df1, df2], axis=1)
print(df.head())

print(df['target'].value_counts())

##############################################################################################################
import matplotlib.pyplot as plt

plt.scatter(df['f1'], df['f2'], c=df['target'])
plt.show()
#############################################################################################################
from imblearn.over_sampling import SMOTE

## Transfer the dataset
oversample = SMOTE()
X, y = oversample.fit_resample(df[['f1', 'f2']], df['target'])

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
df_oversampling = pd.concat([df1, df2], axis=1)
plt.scatter(df_oversampling['f1'], df_oversampling['f2'], c=df_oversampling['target'])
plt.show()