import seaborn as sns

df=sns.load_dataset('titanic')
print(df.head())

### Checking the missing values
print("Total null values in dataset: ",df.isnull().sum().sum())
print(df.isnull().sum())

### Delete the rows -> can lose huge amount of data
df.dropna()

### Delete the column -> can lose important column like age
df.dropna(axis=1)

