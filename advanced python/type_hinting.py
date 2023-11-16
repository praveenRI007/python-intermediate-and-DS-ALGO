def myfunction(parameters : int) -> int:
    return parameters**2

def myfunction1(parameters : list[int]) -> int:
    sum = 0
    for i in parameters:
        sum += i
    return sum
print(myfunction(10))
print(myfunction1([1,2,3,4,5,6,7,8,9,10]))

#mypy type_hinting.py