#  5. Sum of all prime numbers between 1 to n

def prime(num):
    sum=0
    for i in range(2,num+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            sum+=i
    print(f'Sum of first {num} no is:',sum)

num=int(input("Enter no upto you want sum of prime no:"))
prime(num)