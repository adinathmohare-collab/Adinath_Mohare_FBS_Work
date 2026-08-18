from Emp import Emp

class Hr(Emp):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com = com
    def calsal(self):
        return self.sal+self.com
    def __str__(self):
        return super().__str__()+f'\tCom:{self.com}\tFinal Salary:{Hr.calsal(self)}'
    def __repr__(self):
        return self.__str__()