# WAP to check if given number is Perfect Number.

num = int(input("Enter a number: "))

sumofdiv = 0

for i in range(1, num):
    if num%i == 0:
        sumofdiv += i

if sumofdiv == num:
    print(num,"is a Perfect Number.")
else:
    print(num,"is not a Perfect Number.")