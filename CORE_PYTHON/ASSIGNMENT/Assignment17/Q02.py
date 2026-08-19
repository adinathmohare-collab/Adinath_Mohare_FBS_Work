# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

class Student:

    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print(f"Student ID : {self.StudentId}")
        print(f"Name : {self.Name}")
        print(f"Age : {self.Age}")
        print(f"Percentage : {self.Percentage}")

    def CalculateRank(self):
        print("Student Rank Calculated")

    def __str__(self):
        return f"Student ID:{self.StudentId}, Name:{self.Name}, Age:{self.Age}, Percentage:{self.Percentage}"


class EnggStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):

        super().__init__(StudentId, Name, Age, Percentage)

        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Accept(self):

        super().Accept()

        self.Branch = input("Enter Branch: ")
        self.InternalMarks = int(input("Enter Internal Marks: "))

    def Display(self):

        super().Display()

        print(f"Branch : {self.Branch}")
        print(f"Internal Marks : {self.InternalMarks}")

    def CalculateRank(self):

        if self.Percentage >= 90 and self.InternalMarks >= 25:
            print("Rank : 1")

        elif self.Percentage >= 75:
            print("Rank : 2")

        elif self.Percentage >= 60:
            print("Rank : 3")

        else:
            print("Rank : 4")

    def __str__(self):

        return f"Student ID:{self.StudentId}, Name:{self.Name}, Age:{self.Age}, Percentage:{self.Percentage}, Branch:{self.Branch}, Internal Marks:{self.InternalMarks}"


e1 = EnggStudent(101, "Saurabh", 21, 88, "Computer", 28)

e1.Display()

print()

e1.CalculateRank()

print()

print(e1)