import time
import sys
from functools import lru_cache
import concurrent.futures
import multiprocessing

# default is 1000
sys.setrecursionlimit(10000)

# get heap memory size : psutil.virtual_memory().total/(1024.**3)

# without multithreading


@lru_cache
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


def recur_factorial_m(n):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p






if __name__ == '__main__':


    start = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        result = executor.map(recur_factorial_m, [i for i in range(1, 10000)])

    end = time.time()

    print("with multiprocessing - process took:", (end - start), "seconds")

    result = []

    start = time.time()
    for i in range(1,10000):
        result.append(recur_factorial_m(i))

    end = time.time()

    print("without multiprocessing - process took:", (end - start), "seconds")

# for n = 5000
# with multiprocessing - process took: 4.235995769500732 seconds
# without multiprocessing - process took: 8.049002408981323 seconds

# n = 10,000
# with multiprocessing - process took: 19.73799991607666 seconds
# without multiprocessing - process took: 65.79499959945679 seconds

# hence we can see the difference in using multiprocessing



