# 1. Write a program to find sum of following series using recursive functions:
#   i. 1! + 2! + 3! + 4! +..... + n!

def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)


def sum_fact(n):
    if n == 1:
        return 1

    return fact(n) + sum_fact(n - 1)


n = int(input("Enter n: "))
print(sum_fact(n)) 