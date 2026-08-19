#  6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fabo(n):
    a=0
    b=1
    c=1
    print(c)
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c

n=int(input("Enter no: "))
fabo(n)