# 7. Python Program to Find the Intersection of Two Lists 

# 6. Python Program to Find the Union of two Lists

def union_list(li1,li2,intersection):
    for i in li1:
        if i in li2:
            intersection.append(i)

    # for j in li2:
    #     if j in intersection:
    #         intersection.append(j)

li1 = [10,20,30,35,50,55]
li2 = [5,10,15,20,25,30,35]
intersection = []
print("List 1: ",li1)
print("List 2: ",li2)
union_list(li1,li2,intersection)
print("intersection list:",intersection)
