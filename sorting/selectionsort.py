import random
import time

def selectionsort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = random.sample(range(0,1000),1000)
start = time.time()
selectionsort(arr)
end = time.time()
print("The time of execution of insertion sort program is :",
      (end-start) * 10**3, "ms")
#print(arr)
