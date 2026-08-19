# 2. Python Program to Merge Two Lists and Sort it

def merge_and_sort(li1,li2,merged):
    
    merged = li1 + li2
    # print(merged)
    merged.sort()
    return merged



li1 = [5,15,25,35,45,55]
li2 = [10,20,30,40,50]
print("List 1: ",li1)
print("List 2: ",li2)
merged = []
li = merge_and_sort(li1,li2,merged)
print("Sorted merged list: ",li)