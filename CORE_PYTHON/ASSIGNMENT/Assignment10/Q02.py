# 2. Write a program to find maximum and minimum element in a list.

def maximum(li):
    max = li[0]
    for i in li:
        if i > max:
            max = i
    return max

def minimum(li):
    min = li[0]
    for i in li:
        if i < min:
            min =i
    return min


li = [10,30,20,80,55]
print("Maximum no:",maximum(li))
print("Minimum no:",minimum(li))