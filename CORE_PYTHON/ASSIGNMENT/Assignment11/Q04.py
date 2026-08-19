# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort 

def Bubblesort(li):
    size = len(li)
    for i in range(size):
        for j in range(0,size-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]


li = [20,10,33,1,90]
print("List before sort: ",li)
Bubblesort(li)
print("List after bubble sort: ",li)
print("Second last element in list: ",li[-2])
