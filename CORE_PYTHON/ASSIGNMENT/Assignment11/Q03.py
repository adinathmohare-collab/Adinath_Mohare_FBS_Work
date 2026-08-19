# 3. Python Program to Sort the List According to the Second Element in Sublist

def sort(li):
    li.sort(key = lambda x: x[1])
    return li

li = [[20,10,32],[8,2,4],[32,55,1]]
print("Original list: ",li)
sort(li)
print("Sorted list: ",li)