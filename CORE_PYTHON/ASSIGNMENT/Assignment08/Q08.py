#  8. Write a program find reverse of a number

def reverse(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        temp//=10
        rev=rev*10+d
    return rev

num=int(input("Enter no to reverse it:"))
rev=reverse(num)
print("Reversed no is:",rev)