#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 

g=input("Enter the Gender Male or Female:")
age=int(input("Enter the age:"))

if(g=="Female"):
    if("age>=18"):
        print("Eligible for married")
    else:
        print("Not Eligible for married")
elif(g=="Male"):
    if("age>=21"):
        print("Eligible for married")
    else:
        print("Not Eligible for married")
else:
    print("You Enter Wrong Gender ")