# Protected Access Modifier:
# The members of a class that are declared protected are only accessible to a class derived from it.
# Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.


# Private Access Modifier:
# The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
# Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.

class Person:

    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self,value):
        self.__name = value

    @staticmethod
    def my_method():
        print('hello from static')


Person.my_method()

p1 = Person("mike",20,'m')

print(p1.Name)

p1.Name = 'Bob'

print(p1.Name)

