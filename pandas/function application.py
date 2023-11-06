import pandas as pd
import numpy as np

# table wise function application


def adder(ele1,ele2):
    return ele1+ele2


df = pd.DataFrame({"col1":[1,2,3,4,5],"col2":[1,2,3,4,5],"col3":[1,2,3,4,5]},columns=['col1','col2','col3'])

print(df.pipe(adder,2))

# row wise or column wise function application :
# default column wise
print(df.apply(np.mean))
# rowise
print(df.apply(np.mean,axis=1))

print(df.apply(lambda x: x.max() - x.min())) # column wise


# Element Wise Function Application

print(df['col1'].map(lambda x:x*100))

print(df.applymap(lambda x:x*10))





