#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

#Take input from user
a=int(input("Enter the 1st angle:"))
b=int(input("Enter the 2nd angle:"))
c=int(input("Enter the 3rd angle:"))
T=a+b+c
if(T==180):
    print("Triangle is valid")
else:
    print("Triangle is not valid")