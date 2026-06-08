# program_06_Employee_abstraction.py

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):

        print("Developer Writes Code")


obj = Developer()

obj.work()