from abc import ABCMeta
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in function %(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG,
                    filename='../temp.log')


logger = logging.getLogger(__name__)


class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        pass


class Person(IPerson):

    def person_method(self):
        print("im a person !")


class ProxyPerson(IPerson):
    def __init__(self,id):
        self.person = Person()
        self.id = id

    def person_method(self):
        logger.debug("entered proxy")
        print('im the proxy functionality with overriding id:'+str(self.id))
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson(123)
p2.person_method()
