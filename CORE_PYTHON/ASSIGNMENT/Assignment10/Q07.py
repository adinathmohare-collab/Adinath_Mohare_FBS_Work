# 7. Write a program to create a new list from existing list which contains cube of  each number of list.

def cube(li):
    lcube = []
    for i in li:
        lcube.append(i**3)
    return lcube

l = [2,8,1,9,5,22,4]
print("Original list:",l)
print("Cube of list:",cube(l))