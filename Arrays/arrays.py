import array

from matplotlib import pyplot as plt

arr = array.array('i',[1,2,3])

print("newly created array is:",end=" ")
for i in arr:
    print(i,end=" ")

# using append() to insert new value at end
arr.append(4)

# inserting an element at a specified index in an array
arr.insert(2, 5)

print('\r')
# using pop() to remove element at 2nd position
print("The popped element is : ", end="")
print(arr.pop(2))

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# using index() to print index of 1st occurrence of 2
print ("The index of 1st occurrence of 2 is : ", end="")
print (arr.index(2))

# using reverse() to reverse the array
arr.reverse()

print("finally created array is:", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end=" ")


