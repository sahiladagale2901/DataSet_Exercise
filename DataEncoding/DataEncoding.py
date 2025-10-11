'''
Nominal/ OHE (One Hot) Encoding
'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Create
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue']
})

# Create an instance of OHE
encoder = OneHotEncoder()

## Perform fit_transform
encoded = encoder.fit_transform(df[['color']]).toarray()
print(encoded)

encoder_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
print(encoder_df)

# For New Data
arr = encoder.transform([['red']]).toarray()
print(arr)

# OR
new_data = pd.DataFrame({'color': ['red', 'blue']})
arr = encoder.transform(new_data[['color']]).toarray()
print(arr)

dataFrame = pd.concat([df, encoder_df], axis=1)
print(dataFrame)

######################################################################################################################
'''

Label Encoding- involves assigning a unique numerical label to each category in the variable.

Red: 1
Green: 2
Blue: 3

But here Machine thinks blue>green>red on the basics of values assigned.
'''

print("#########################" * 5)
print(df)

from sklearn.preprocessing import LabelEncoder

lbl_encoder = LabelEncoder()

df_label_encoder = lbl_encoder.fit_transform(df[['color']])
print(df_label_encoder)

print(lbl_encoder.transform([['red']]))
######################################################################################################################
'''

Ordinal Encoding- Categorical data have intrinsic order and ranking. assigned unique value based on the order

example:
highSchool: 1
college: 2
UG: 3
PG:4
'''
print("#########################" * 5)
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({
    'size': ['small', 'medium', 'large', 'small', 'large', 'medium']
})

## create instance
encoder = OrdinalEncoder(categories=[['small', 'medium', 'large']])
encoder_ordinal = encoder.fit_transform(df[['size']])
print(encoder_ordinal)

print(encoder.transform([['small']]))
print(encoder.transform([['large']]))
######################################################################################################################
'''

Target Guided Ordinal Encoding- Categorical variable based on the their relationship with target variable.
                                Useful when - Categorical variable with large number of unique categories

Replace each category in the categorical variable with the numerical values based on
the mean median of the target variable of the category
'''
print("#########################" * 5)

df = pd.DataFrame({
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'New York', 'Tokyo'],
    'price': [200, 150, 300, 450, 250, 180]
})

mean_price = df.groupby('city')['price'].mean().to_dict()
print(mean_price)
df['city_encoded']=df['city'].map(mean_price)
print(df)
