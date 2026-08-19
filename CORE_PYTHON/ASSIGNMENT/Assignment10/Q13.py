# 13 . Write a program to print list after removing even numbers.

def remove_even(li,new):
    for i in range(len(li)):
        if i % 2 != 0:
            new.append(i)
            

li = [2,3,4,5,6,7,8,9,10]
new = []
remove_even(li,new)
print("Original list: ",li)
print("List after removing even no: ",new)
