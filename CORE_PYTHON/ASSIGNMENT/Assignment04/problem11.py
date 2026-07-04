# WAP to check if given number Strong Number.

num = int(input("Enter a number:"))
temp = num
sumoffact = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sumoffact += fact
    temp //= 10

if sumoffact == num:
    print(num, "is a Strong Number.")
else:
    print(num,"is not a Strong Number.")