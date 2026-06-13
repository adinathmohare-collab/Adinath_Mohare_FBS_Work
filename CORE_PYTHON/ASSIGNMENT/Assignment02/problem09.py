#9. Write a program to swap two numbers without using third variable.
a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))

print("Before swaping::",a,b)

a=a+b        #30=10+20
b=a-b        #20=20-10
a=a-b        #30=30-10

print("After the swaping::",a,b)