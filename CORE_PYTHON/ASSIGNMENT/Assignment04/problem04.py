# 4. WAP to print factorial of a number .
n=int (input ("Enter the number:"))
m=n
for i in range (1,n):
    n *=i
    i +=1
print("factorial is:",n)