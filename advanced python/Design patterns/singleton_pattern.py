from datetime import datetime
from abc import ABCMeta


class ILogger(metaclass=ABCMeta):
    @staticmethod
    def log_data():
        """log the data"""
        pass


class PersonSingleton(ILogger):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("default Name",0)
        return PersonSingleton.__instance

    def __init__(self,name,age):
        if PersonSingleton.__instance is not None:
            raise Exception("singleton cannot be raised more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def log_data():
        print(f"Name: {PersonSingleton.__instance.name} age: {PersonSingleton.__instance.age} logged datetime : {datetime.now()}")


p = PersonSingleton("Mike",30)
print(p)
p.log_data()

#p = PersonSingleton("Mike2",30) # error : raise Exception("singleton cannot be raised more than once")


