# 6. Python Program to Find the Union of two Lists

def union_list(li1,li2,union):
    for i in li1:
        if i not in union:
            union.append(i)

    for j in li2:
        if j not in union:
            union.append(j)

li1 = [10,20,30,35,50,55]
li2 = [5,10,15,20,25,30,35]
union = []
print("List 1: ",li1)
print("List 2: ",li2)
union_list(li1,li2,union)
print("Union list:",union)
