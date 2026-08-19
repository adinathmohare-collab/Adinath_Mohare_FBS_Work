# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f'sum from 1 to upto {n} is: {sum}')


def fact(n):
    sum=0
    for i in range(1,n+1):
        fact=1
        for j in range(1,i+1):
            fact=fact*j
        sum=sum+fact
        # print(f'Factorial of {i} is: {fact}')
    print(f'sum of factorial upto {n} is {sum}')


def expo(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**i
    print(f'addotion is {sum}')
    


n=int(input("Enter any no: "))
sum(n)
fact(n)
expo(n)