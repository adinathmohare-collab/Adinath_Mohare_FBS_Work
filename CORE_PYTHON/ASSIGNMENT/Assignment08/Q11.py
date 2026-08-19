#  11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def power(n):
    tmp=n
    i=0
    while(tmp>0):
        i+=1
        tmp//=10
    return i

def Armstrong(n,i):
    temp=n
    sum=0
    while(temp>0):
        d=temp%10
        temp//=10
        sum+=d**i
    if sum==n:
        print("No is armstrong")
    else:
        print("No is not armstrong")


n=int(input("Enter no to check no is armstrong or not :"))
i=power(n)
Armstrong(n,i)