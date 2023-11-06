import pandas as pd
import numpy as np
# df = pd.DataFrame({"S.No":[1,2,3,4],
#                    "Name":['Tom','Lee','Steven','Ram'],
#                    "Age":[28,32,43,37],
#                    "City":['Toronto','HongKong','Bay Area','Hyderabad'],
#                    "Salary":[20000,3000,8300,3900]
#                    })
#
# df.to_csv('temp.csv')

df=pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print(df.dtypes)

df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
print(df)

# if the header is in a row other than the first, pass the row number to header. This will skip
# the preceding rows.

df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
print(df)

# skip rows

df=pd.read_csv("temp.csv", skiprows=2)
print(df)