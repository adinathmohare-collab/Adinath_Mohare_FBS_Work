# 2. Write a program to check if given number is Armstrong or not using recursive function.
def arm(temp, count):
    if temp == 0:
        return 0

    d = temp % 10

    return d ** count + arm(temp // 10, count)


n = int(input("Enter number: "))

count = len(str(n))

if arm(n, count) == n:
    print("Armstrong")
else:
    print("Not Armstrong")