import pandas as pd
import numpy as np
# pandas deals with following data structures

# series : 1D labeled homogeneous array, size-immutable , Values of Data Mutable

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])

data_dict = {'a' : 0., 'b' : 1., 'c' : 2.}


s = pd.Series(data)

f = pd.Series(data,index=[100,101,102,103])

d = pd.Series(data_dict)  # dict keys are used to construct index

sca = pd.Series(5, index=[0, 1, 2, 3])  # create series using scalar

s1 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])



#print(s)
#print(f)
#print(d)
#print(sca)

#print(s1[2])
#print(s1[:3])

# A Series is like a fixed-size dict in that you can get and set values by index label.
#print(s1['a'])
#print(s1[['a','b','c']])

# if key not there then error is raised : keyerror




# dataframe : General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed columns

# pandas df can be created using various inputs like lists,  dict , Series , Numpy ndarrays , another dataframe

# from list
data = [1,2,3,4,5]
df_list = pd.DataFrame(data)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])

df = df.astype(dtype={'Age':float}) # set column's datatype


#print(df_list)
print(df)

# from dict

data_dict = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}

df_dict = pd.DataFrame(data_dict)
df_dict_updated_index = pd.DataFrame(data_dict, index=['rank1','rank2','rank3','rank4'])


#print(df_dict)
#print(df_dict_updated_index)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'],columns=['a', 'b','c'])
#print(df)

# df from dict of series

data2 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data2)
#print(df)

# column selection

#print(df['one'])

# column addition

df['three']=pd.Series([10,20,30],index=['a','b','c'])

#print(df)

df['four']=df['one']+df['three']

#print(df)

# column deletion

del df['four']
df.pop('two')


#print(df)


# selection by Label
# Rows can be selected by passing row label to a "loc" function.

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)


#print(df.loc['b'])

# Selection by integer location
# Rows can be selected by passing integer location to an iloc function.

#print(df.iloc[2])

# slice rows

#print(df[2:4])

# add rows at the end

df2 = pd.DataFrame({'three':pd.Series([1,2,3],index=['a', 'b', 'c'])})

df =  pd.concat([df,df2],axis=1,join='inner')

#print('******************************')
#print(df)

# deletion of rows

#df = df.drop('a')
df.drop('a',inplace = True)

#print(df)

# panel : General 3D labeled, size-mutable array , data mutable






