# seq 1 to 9,000,000

def my_generator(n):
    for x in range(1,n):
        yield x ** 3


values = my_generator(100)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

for x in values:
    print(x)


def infinite_seq():
    res = 1
    while True:
        yield res
        res *= 5

val = infinite_seq()

print(next(val))
print(next(val))
print(next(val))

