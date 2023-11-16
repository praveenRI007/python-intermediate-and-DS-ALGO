class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vector(self.x + other.x,self.y + other.y)

    def __repr__(self):
        return f"X:{self.x} , Y:{self.y}"

    def __call__(self):
        print(f"hello i was called !!! x:{self.x} , y:{self.y}")


v1 = vector(10,20)
v2 = vector(20,20)

v3 = v1 + v2

v3()


# hello i was called !!! x:30 , y:40