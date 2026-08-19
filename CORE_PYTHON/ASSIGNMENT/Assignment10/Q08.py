# 8. Write a program to create a duplicate of an existing list. It should not point to same list. 

def duplicate(li1):
    dlist = []
    for i in li1:
        dlist.append(i)
    return dlist


li1 = [10,20,30,40,50]
Dlist = duplicate(li1)
print(f'Original list: {li1} and its address {id(li1)}')
print(f'Duplicate list: {Dlist} and its address {id(Dlist)}')


# print(id(li1))

# li2 = li1.copy()
# print(id(li2))

# li2.append(111)
# print(li1)