#  4. Sum of all odd numbers between 1 to n

def odd(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    return sum

n=int(input("Enter no to find sum of odd no upto no:"))
res=odd(n)
print("Addition is:",res)