# .loc() Label based
# .iloc() Integer based
# .ix() Both Label and Integer based its depreciated use loc instead

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4),index=['a','b','c','d','e','f','g','h'], columns=['A', 'B', 'C', 'D'])

# select all rows for a specific column
print(df.loc[:,'A'])

# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])

# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])

# Select range of rows for all columns
print(df.loc['a':'h'])

# for getting values with a boolean array
print(df.loc['a']>0)


df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])

print(df)
# select all rows for a specific column
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])
print(df.iloc[[1, 3, 5], [1, 3]])



print(df.loc[:,'A'])

print(df[1:3])





