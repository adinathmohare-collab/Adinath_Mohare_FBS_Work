# 6. Write a program to remove duplicates from the list. 

def unique(li):
    ulist = []
    for i in li:
        if i not in ulist:
            ulist.append(i)
    return ulist



li = [2,8,33,9,5,2,9,2,11]
print('List with duplicates:',li)
print('List without duplicates:',unique(li))
# s = set(li)
# a = list(s)
# print(a)