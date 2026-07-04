# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


# a. 1! + 2! + 3! + 4! + .....n!

n=int(input("Enter no upto you want addition of factorial! "))
s=0
for i in range(1,n+1):
    t=1
    for j in range(1,i+1):
        t=t*j
    print(i,"!=",t)
    s+=t
    print("sum of factorial upto ",n,"is",s)



# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n=int(input("Enter no which you want to calculate exponent: "))
s=0
for i in range(1,n+1):
    t=n
    # for j in range(1,i):
    s+=t**i
print(s)



# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# 1+2+4+8+16+32  each value is *2 of previous value

n=int(input("Enter no upto you want geometric sum: "))
sum=0
p=1
for i in range(1,n+1):
    # print(t)
    sum+=p
    p*=2
print(sum)



# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a=int(input("Enter no you want to calculate series of no^i/i: "))
s=0
for i in range(1,11):
    s+=(a**i)/i
print(s)



# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x=int(input("Enter any no you want to calculate series no^i/odd_no "))
n=int(input("Enter no upto you want series: "))
sum=0
e=1
for i in range(1,n+1):
    if i%2==0:
        sum-=x**i/e
    else:
        sum+=x**i/e
    e+=2
print(sum)
