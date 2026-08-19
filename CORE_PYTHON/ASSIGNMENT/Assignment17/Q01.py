# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:
    def __init__(self,StudentId,Name,Age,Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 90:
            print('Rank:1')
        elif self.Percentage >= 75:
            print('Rank:2')
        elif self.Percentage >= 60:
            print('Rank:3')
        else:
            print('Rank:4')

    def Display(self):
        print(f'StudentId:{self.StudentId}\tName:{self.Name}\tAge:{self.Age}\tPercentage:{self.Percentage}')

    def __str__(self):
        return f"Student ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}"

s1 = Student(101, "Saurabh", 21, 88)
print(s1)
s2 = Student(0,'',0,0)
s2.Accept()
print(s2)