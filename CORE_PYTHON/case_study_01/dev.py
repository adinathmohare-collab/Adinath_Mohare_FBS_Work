from Emp import Emp

class Dev(Emp):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus = bonus
    def calsal(self):
        return self.sal+self.bonus
    def __str__(self):
        return super().__str__()+f'\tBonus:{self.bonus}\tFinal Salary:{Dev.calsal(self)}'

    def __repr__(self):
        return self.__str__()