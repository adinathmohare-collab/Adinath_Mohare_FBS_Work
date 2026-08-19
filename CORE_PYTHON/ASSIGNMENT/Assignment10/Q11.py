# 11. Write a program to print all numbers which are divisible by m and n in the list. 


def divide(li,m,n):
    for i in range(len(li)):
        if  li[i] % m == 0  and li[i] % n == 0:
            print(li[i])

li = [2,4,5,8,9,14,99,45,6]
m = int(input("Enter 1st value by you want to divide: "))
n = int(input("Enter 2nd value by you want to divide: "))
divide(li,m,n)