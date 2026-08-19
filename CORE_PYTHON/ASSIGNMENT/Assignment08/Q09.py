#  9. Write a program to check if entered number is a palindrome or not.

def palindrome(n):
    rev=0
    tp=n
    while(tp>0):
        d=tp%10
        tp//=10
        rev=rev*10+d
    if rev==n:
        return True
    else:
        return False

n=int(input("Enter no to check no is pallindrome or not: "))
pal=palindrome(n)
if pal==True:
    print("No is pallindrome")
else:
    print("No is not pallindrome")