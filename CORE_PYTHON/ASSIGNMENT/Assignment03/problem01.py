#1. Write a program to check if the given number is positive or negative. 

#Take input from user
num=int(input("Enter the number"))

if(num>0):
    print("Number is positive.")
elif(num<0):
    print("Number is negative.")
else:
    print("Number is neutral.")