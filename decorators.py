def permission(msg1):
    print(msg1)
    def wrap(fun):
        def wrapper(*args,**kwargs):
            id , name = args
            if id == 4 and name == 'praveen':
                print('permission granted')
            else:
                print('invalid')

            return fun(*args,**kwargs)
        return wrapper
    return wrap


@permission("Entered permission function")
def ful(id,name):
    print(f'hi this is {name} here')


ful(4,"praveen")