#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=int(input("Enter the 1st side:"))
b=int(input("Enter the 2nd side:"))
c=int(input("Enter the 3rd side:"))

if(a==b==c):
    print("This is equilateral triangle")
elif(a==b or b==c or a==c):
    print("This is isoscales triangle ")
else:
    print("This is scalene triangle")
