# Write a program to area of triangle and rectangle

#Take input from user

base=float(input("Enter the base:"))
height=float(input("Enter the height:"))
l=float(input("Enter the length:"))
b=float(input("Enter the breadth:"))

#perform operations
T=(1/2)*base*height
R=l*b

#Display output
print(f"Area of Triangle is{T}")
print(f"Area of Rectangle is{R}")