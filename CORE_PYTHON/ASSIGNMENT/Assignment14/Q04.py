# 4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.


lst = [1, 2, 3, 4, 5, 6]
print(lst)

n = int(input("Enter no to find sum equal to pair of elements: "))

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j] == n:
            print(f'{lst[i],lst[j]}')