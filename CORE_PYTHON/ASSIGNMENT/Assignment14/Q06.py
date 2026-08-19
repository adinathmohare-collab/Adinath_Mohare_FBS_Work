# 6. Write a Python program to find the two numbers whose product is maximum among 
# all the pairs in a given list of numbers. Use the Python set.

# lst = [2, 5, 12, 7, 9, 10]
lst=[]
n= int(input("Enter no of elements to add to list: "))
for i in range(n):
    no = int(input("Enter no to add in list:"))
    lst.append(no)

print(lst)
max_product = lst[0]*lst[1]
num1=lst[0]
num2=lst[1]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]*lst[j] > max_product:
            max_product = lst[i]*lst[j]
            num1=lst[i]
            num2=lst[j]

print(f'Pair of no whose product is maximum:{(num1,num2)}')
print(f'Maximum product:{max_product}')
