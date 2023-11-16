
class Foo:
    def show(self):
        print('hi')


def add_attribute(self):
    self.z = 9


test = type('Test',(Foo,),{'x':5,"add_attribute":add_attribute})
t = test()
print(t.x)
t.show()
t.add_attribute()
print(t.z)


class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)

        a = {}
        for name,value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name,bases,attrs)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print('hi')


d = Dog()
print(d.x)

