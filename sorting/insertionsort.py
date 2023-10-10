import random
import time
def insertionsort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



arr = random.sample(range(0,1000),1000)
start = time.time()
insertionsort(arr)
end = time.time()
print("The time of execution of insertion sort program is :",
      (end-start) * 10**3, "ms")
#print(arr)
