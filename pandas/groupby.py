# Any groupby operation involves one of the following operations on the original object.
# They are:
#  Splitting the Object
#  Applying a function
#  Combining the results

# In many situations, we split the data into sets and we apply some functionality on each
# subset. In the apply functionality, we can perform the following operations:
#  Aggregation - computing a summary statistic
#  Transformation - perform some group-specific operation
#  Filtration - discarding the data with some condition

import pandas as pd
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
 'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
 'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
 'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
#print(df)

# split data into groups

#print(df.groupby('Team').groups)

# group by multiple columns

#print(df.groupby(['Team','Year']).groups)

# iterating through groups

groups = df.groupby('Year')

for name,group in groups:
    pass
    print(name)
    print(group)

#print('*******************************')
# select a group
#print(groups.get_group(2014))

import numpy as np
# aggregations
#print(groups['Points'].agg(np.mean))

#print(groups.agg(np.size))

# applying multiple aggregations at once

#print(groups['Points'].agg([np.sum,np.mean,np.std]))

# Transformations
grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10

#print(grouped.transform(score))


# filterations
#print(df.groupby('Team').filter(lambda x: len(x) >= 3)) # teams which have participated 3 or more times





