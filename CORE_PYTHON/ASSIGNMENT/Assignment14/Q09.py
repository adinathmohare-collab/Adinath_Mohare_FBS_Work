# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

lst = []

n = int(input("Enter number of elements: "))

for i in range(n):
    no = int(input("Enter element: "))
    lst.append(no)

target = int(input("Enter target sum: "))

print("List:", lst)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
            if lst[i] + lst[j] + lst[k] == target:
                print(f'{lst[i],lst[j],lst[k]}')