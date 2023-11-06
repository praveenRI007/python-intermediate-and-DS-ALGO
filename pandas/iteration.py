import pandas as pd
import numpy as np

# no changes will update while trying to update while iterating

N=20
df = pd.DataFrame({
 'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
 'x': np.linspace(0,stop=N-1,num=N),
 'y': np.random.rand(N),
 'C': np.random.choice(['Low','Medium','High'],N).tolist(),
 'D': np.random.normal(100, 10, size=(N)).tolist()
 })

# gives column names
for col in df:
    print(col)


# o iterate over the rows of the DataFrame, we can use the following functions:
#  iteritems() - to iterate over the (key,value) pairs
df=pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print(df)
for key,value in df.items():
    print(key,value)

#  iterrows() - iterate over the rows as (index,series) pairs
print("\n")
for row_index,row in df.iterrows():
    print(row_index,row)

#  itertuples() - iterate over the rows as namedtuples
for row in df.itertuples():
    print(row)


