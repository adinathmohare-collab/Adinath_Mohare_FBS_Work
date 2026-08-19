# 7. Write a program to find sum of digits using recursion.

def sum_of_digit(n):
    if n==0:
        return 0
    return n % 10 + sum_of_digit(n//10)

n = int(input("Enter no to find sum of digits: "))
res = sum_of_digit(n)
print("Sum: ",res)

