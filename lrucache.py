import sys
from functools import lru_cache
import time
sys.setrecursionlimit(10000)


# Function that computes Fibonacci
# numbers without lru_cache
def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


# Execution start time
begin = time.perf_counter()
fib_without_cache(10)
# Execution end time
end = time.perf_counter()

print("Time taken to execute the\
function without lru_cache is", end - begin)

# Function that computes Fibonacci
# numbers with lru_cache

# maxsize=128


@lru_cache(maxsize=10000)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)


begin = time.perf_counter()
fib_with_cache(500)
end = time.perf_counter()

print("Time taken to execute the \
function with lru_cache is", end - begin)
