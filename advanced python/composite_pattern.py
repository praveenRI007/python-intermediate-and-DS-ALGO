from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ implement in child class"""
        pass

    @staticmethod
    def print_department():
        """implement in child class"""
        pass


class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Deparment: {self.employees}")


class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department (self):
        print(f"Development Deparment: {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self,dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("parent department")
        print(f"Parent department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"total no of employees: {self.employees}")


dep1 = Accounting(200)
dep2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dep1)
parent_dept.add(dep2)

parent_dept.print_department()