from abc import ABCMeta


class IPerson(metaclass=ABCMeta):
    @staticmethod
    def person_method():
        pass


class Student(IPerson):
    def __init__(self):
        self.name = "default name"

    def person_method(self):
        print("im a student")


class Teacher(IPerson):
    def __init__(self):
        self.name = "default teacher name"

    def person_method(self):
        print("im a teacher")


s1 = Student()
s1.person_method()

t1 = Teacher()
t1.person_method()


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == 'Teacher':
            return Teacher()

        print("invalid type")
        return -1


if __name__ == '__main__':
    choice = input('what person you want to create?\n')
    person = PersonFactory.build_person(choice)
    person.person_method()