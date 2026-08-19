#  10. Write a program to check if entered year is a leap year or not.

def leap(year):
    if year % 4==0 and year%100!=0 or year%400==0:
        print("Year is leap year") 
    else:
        print("Year is not leap year")

y=int(input("Enter year to check leap or not: "))
leap(y)