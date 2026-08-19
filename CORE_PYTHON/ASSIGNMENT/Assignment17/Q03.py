# 3. Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
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


class MedicalStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage, Specialization, MarksOfInternship):

        super().__init__(StudentId, Name, Age, Percentage)

        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def Accept(self):

        super().Accept()

        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = int(input("Enter Internal Marks: "))

    def Display(self):

        super().Display()

        print(f"Specialization : {self.Specialization}")
        print(f"Internal Marks : {self.MarksOfInternship}")

    def CalculateRank(self):

        if self.Percentage >= 90 and self.MarksOfInternship >= 25:
            print("Rank : 1")

        elif self.Percentage >= 75:
            print("Rank : 2")

        elif self.Percentage >= 60:
            print("Rank : 3")

        else:
            print("Rank : 4")

    def __str__(self):

        return f"Student ID:{self.StudentId}, Name:{self.Name}, Age:{self.Age}, Percentage:{self.Percentage}, Specialization:{self.Specialization}, Internal Marks:{self.MarksOfInternship}"


e1 = MedicalStudent(101, "Saurabh", 21, 95, "Cardiology", 82)

e1.Display()

print()

e1.CalculateRank()

print()

print(e1)