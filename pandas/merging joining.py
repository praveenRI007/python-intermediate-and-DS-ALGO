# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
# left_index=False, right_index=False, sort=True)

import pandas as pd

left = pd.DataFrame({
 'id':[1,2,3,4,5],
 'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
 'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
 {'id':[1,2,3,4,5],
 'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
 'subject_id':['sub2','sub4','sub3','sub6','sub5']})

print(pd.merge(left,right,on=['id','subject_id']))

# merge :   left, right , outer , innner

# left join
print(pd.merge(left,right,on='subject_id',how='left'))

# right join
print(pd.merge(left,right,on='subject_id',how='right'))

# outer join
print(pd.merge(left, right, how='outer', on='subject_id'))

# inner join
print(pd.merge(left, right, on='subject_id', how='inner'))



