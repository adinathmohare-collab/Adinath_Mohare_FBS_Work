# WAP to print all numbers in a range divisible by a given number.

st = int(input("Enter starting of range: "))
end = int(input("Enter ending of range: "))
n = int(input("Enter the divisor: "))

print("Numbers divisible by", n, "are:")

for i in range(start,end + 1):
    if i%n == 0:
        print(i,end=" ")