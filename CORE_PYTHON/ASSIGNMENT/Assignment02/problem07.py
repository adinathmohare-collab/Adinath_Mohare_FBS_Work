#Find the sum of three digit no.

#Take input from user
num=int(input("Enter three digits no:"))

#perform operations
d1=num % 10 # to seperate first digit in the number
num=num // 10

d2=num % 10 # to seperate second digit in the number
num=num // 10

d3=num % 10 # to seperate third digit in the number
num=num // 10

sum=d1+d2+d3 # sum of the digits

#display sum
print("Sum of three digits is:",sum)