#12. Write a program to check if given 3 digit number is a palindrome or not.

num=int(input("Enter the 3 digit number:"))
f1=num // 10
r1=num % 10
f2=f1 // 10

if(r1==f2):
    print("Palindrome no.")
else:
    print("Not palindrome")