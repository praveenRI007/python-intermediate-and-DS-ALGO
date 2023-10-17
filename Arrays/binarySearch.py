import random
import time
import sys


arr = random.sample(range(0,100000),100000)

def normal_search(elem):
    start = time.time()
    for i in range(0,len(arr)):
        if arr[i] == elem:
            print(f"element \"{str(arr[i])}\" found at index {i}")
    end = time.time()
    print("The time of execution of normal search is :",
          (end - start) * 10 ** 3, "ms")


def binary_search(elem):
    arr.sort()
    start = time.time()
    lo = 0
    hi = len(arr) - 1
    while lo<=hi:
        mid = (hi + lo)//2

        if elem > arr[mid]:
            lo = mid+1
        elif elem < arr[mid]:
            hi = mid - 1
        else:
            print(f"element \"{elem}\" found at index {mid}")
            break

    end = time.time()
    print("The time of execution of binary search is :",
          (end - start) * 10 ** 3, "ms")

normal_search(random.choice(arr))

binary_search(random.choice(arr))
