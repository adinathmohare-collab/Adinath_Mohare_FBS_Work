# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

        
class Student:

    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def __str__(self):
        return f"ID:{self.StudentId}, Name:{self.Name}, Age:{self.Age}, Percentage:{self.Percentage}"


class College:

    def __init__(self, n):
        self.n = n
        self.students = []

    def AddStudent(self, student):

        if len(self.students) < self.n:
            self.students.append(student)
            print("Student Added Successfully")
        else:
            print("College is Full")

    def GetStudent(self, sid):

        for student in self.students:

            if student.StudentId == sid:
                return student

        return "Student Not Found"

    def RemoveStudent(self, sid):

        for student in self.students:

            if student.StudentId == sid:
                self.students.remove(student)
                print("Student Removed")
                return

        print("Student Not Found")

    def __str__(self):

        result = ""

        for student in self.students:
            result += str(student) + "\n"

        return result


college = College(3)

s1 = Student(101, "Saurabh", 21, 88)
s2 = Student(102, "Rahul", 22, 79)
s3 = Student(103, "Amit", 20, 91)

college.AddStudent(s1)
college.AddStudent(s2)
college.AddStudent(s3)

print()

print(college)

print("Searching Student")
print(college.GetStudent(102))

print()

college.RemoveStudent(102)

print()

print(college)