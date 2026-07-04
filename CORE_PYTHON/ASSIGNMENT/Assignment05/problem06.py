# 6. Write a program to print first n prime numbers.

n=int(input("Enter no upto you want prime no: "))

for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)