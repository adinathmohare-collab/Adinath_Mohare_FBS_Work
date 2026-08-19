#  7. Write a program to find sum of digits of a number.

def sum(n):
    t=n
    add=0
    while(t>0):
        d=t%10
        t//=10
        add=add+d
    print("Sum: ",add)

num=int(input("Enter no to find sum of its digit: "))
sum(num)