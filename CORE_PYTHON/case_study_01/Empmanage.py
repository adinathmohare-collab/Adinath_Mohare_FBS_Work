from hr import Hr
from dev import Dev
class Empmanage:
    empDat = {}
    
    def AddEmp(self):
        print('-----Add Employee-----')
        id = int(input('Enter Employee Id: '))
        if id in self.empDat:
            print("Employee already exist")
            return
        name = input("Enter name of Employee:")
        sal = float(input("Enter salary of Employee:"))
        print("1.Hr")
        print("2.Devloper")
        ch = int(input("Enter choice:"))
        if ch ==1:
            com = float(input("Enter commision:"))
            emp = Hr(id,name,sal,com)
        elif ch ==2:
            bonus = float(input("Enter bonus:"))
            emp = Dev(id,name,sal,bonus)
        else:
            print("Invalid choice")
        self.empDat[id] = emp
        print("Employee Added Successfully")


    def SearchEmp(self):

        id = int(input("Enter id of employee to search:"))
        if id in self.empDat:
            print("Employee found\nDetails:")
            print(self.empDat[id])
        else:
            print("Employee not found")


    def DeleteEmp(self):
        id = int(input("Enter id of employee to delete:"))
        if id not in self.empDat:
            print("Employee not found")
        else:
            Empmanage.empDat[id]
            del self.empDat[id]
            print("Employee deleted successfully")        


    def UpdateEmp(self):
        id = int(input("Enter id of employee to update: "))
        if id not in self.empDat:
            print("Employee not found")
            return
        emp = self.empDat[id]
        print("Employee found")
        print("Current Details:")
        print(emp)
        print("\nEnter new details")

        name = input("Enter new name: ")
        sal = float(input("Enter new salary: "))

        emp.name = name
        emp.sal = sal

        if isinstance(emp, Hr):
            com = float(input("Enter new commission: "))
            emp.com = com

        elif isinstance(emp, Dev):
            bonus = float(input("Enter new bonus: "))
            emp.bonus = bonus

        print("Employee updated successfully")


    def DisplayEmp(self):

        if len(Empmanage.empDat)==0:
            print("No employee in system")
        else:
            for emp in Empmanage.empDat.values():
                print(emp)
                
