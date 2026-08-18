from abc import ABC,abstractmethod

class Emp(ABC):
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    # @abstractmethod
    # def calsal(self):
        # pass
    def __str__(self):
        return f'Id:{self.id}\tName:{self.name}\tSalary:{self.sal}'

    # def __repr__(self):
    #     return self.__str__()