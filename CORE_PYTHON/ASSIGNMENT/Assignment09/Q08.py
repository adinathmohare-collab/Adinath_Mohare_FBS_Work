# 8. Write a program to check whether a number is prime or not using recursion. 

def prime(n,i):
    if n<=1:
        return False
    if i == n:
        return True
    if n % i ==0:
        return False
    return prime(n,i+1)
    

n= int(input("Enter no to check prime or not: "))
if  prime(n,2):
    print(f"{n} is prime")
else:
    print(f"{n} is Not prime")