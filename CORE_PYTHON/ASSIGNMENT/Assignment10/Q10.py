# 10. Write a program to remove all occurrences of a given element in the list.


def remove(li,n,new):
    for i in range(len(li)):
        if li[i] != n:
            new.append(li[i])
        
li = [10,20,30,9,33,10]
n=int(input("Enter element you want to remove from list: "))
new = []
remove(li,n,new)
print(new)
