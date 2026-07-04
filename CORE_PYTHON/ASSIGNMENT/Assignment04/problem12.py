# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)

num = int(input("Enter a number: "))

temp = num
digits = len(str(num)) # to store length of the num variable
sumofarm = 0

while temp > 0:
    digit = temp % 10
    sumofarm += digit ** digits
    temp //= 10

if sumofarm == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")