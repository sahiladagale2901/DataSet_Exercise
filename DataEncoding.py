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
