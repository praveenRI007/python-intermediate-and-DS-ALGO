import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)

# check for missing values
print(df['one'].isnull()) #notnull


# cleaning/filling missing data
print("NaN replaced with '0':")
print(df.fillna(0))

# pad/fill       - Fill methods Forward
# bfill/backfill - Fill methods Backward

print(df.fillna(method='pad'))

print(df.fillna(method='backfill'))

# drop missing values
print(df.dropna())



# dropna columnwise
print(df.dropna(axis=1)) # removes all columns , all columns have some na values

# replace missing or generic values
df = pd.DataFrame({'one':[10,20,30,40,50,2000],'two':[1000,0,30,40,50,60]})
print(df.replace({1000:10,2000:60}))
print(df.replace([1000,2000],[10,60]))

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print(df['one'].mean())
print(df.fillna(df.mean(axis=0)))









