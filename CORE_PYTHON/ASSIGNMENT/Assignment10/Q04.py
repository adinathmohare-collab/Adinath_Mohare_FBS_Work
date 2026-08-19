# 4. Write a program to reverse the list.

def reverse(li):
    for i in range(len(li)-1,-1,-1):
        rev.append(li[i])

li = [10,20,50,60,2,44]
rev = []
print('Original list:',li)
reverse(li)
print('Reversed list:',rev)
