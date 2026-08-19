# 4. Write a program to find sum of n numbers using recursion.

def sum_num(n):
    if n == 1:
        return 1

    return n + sum_num(n - 1)

n = int(input("Enter n: "))
print("Sum =", sum_num(n))