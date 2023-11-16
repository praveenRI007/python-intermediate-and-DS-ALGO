from abc import ABCMeta


class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        pass


class Person(IPerson):

    def person_method(self):
        print("im a person !")


class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print('im the proxy functionality')
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
