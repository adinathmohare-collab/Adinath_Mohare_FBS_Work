# 10. Write a program to reverse a number using recursion.

def reverse(n, rev):

    if n == 0:
        return rev

    d = n % 10

    return reverse(n // 10, rev * 10 + d)


n = int(input("Enter number: "))

print(reverse(n, 0))
