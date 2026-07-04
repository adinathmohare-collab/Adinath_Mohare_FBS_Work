# 4. WAP to print Armstrong number within a given range

start=int(input("Enter starting no: "))
end=int(input("Enter ending no: "))
for i in range(start,end+1):
    c=0
    s=0
    t=i
    while(t>0):
        d=t%10
        t//=10
        c+=1
    t=i
    while(t>0):
        d=t%10
        t//=10
        s+=d**c
    if(s==i):
        print(i)


