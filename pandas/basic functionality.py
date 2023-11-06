import pandas as pd
import numpy as np

# Create a series with 100 random numbers

# SERIES

s = pd.Series(np.random.randn(4))
print ("The axes are:")
print(s.axes)

# returns of obj is empty or not
print(s.empty)

# returns dimension of the obj
print(s.ndim)

# returns size of the series
print(s.size)

# returns values in the series as a array/list
print(s.values)

# display head , tail of the series default 5
print(s.head(1))
print(s.tail(1))

# DATAFRAMES

#Create a Dictionary of series
d={'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
'Age':pd.Series([25,26,25,23,30,29,23]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our data series is:")
print(df)

print ("The transpose of the data series is:")
print(df.T)

# returns the list of row axis labels and column axis labels.
print("Row axis labels and column axis labels are:")
print(df.axes)
print ("The data types of each column are:")
print(df.dtypes)

print ("Is the object empty?")
print(df.empty)

print ("The dimension of the object is:")
print(df.ndim)

print("The shape of the object is:")
print(df.shape)

print ("The total number of elements in our object is:")
print(df.size)

print ("The actual data in our data frame is:") # get df values as a list / ndarray
print(df.values)

print ("The last two rows of the data frame is:")
print(df.tail(2))

print ("The first two rows of the data frame is:")
print(df.head(2))



