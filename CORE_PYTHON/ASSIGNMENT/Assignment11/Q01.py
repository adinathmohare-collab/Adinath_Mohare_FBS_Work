# 1. Python Program to Put Even and Odd elements of a List into two Different Lists

def even_odd(li,even,odd):
    for i in range(len(li)):
        if li[i] % 2 == 0:
            even.append(li[i])
        else:
            odd.append(li[i])


li = [1,2,3,4,5,6,7,8,9,10]
# li = [11,22,33,44,55,66]
even = []
odd = []
even_odd(li,even,odd)
print("Original list",li)
print("even list",even)
print("odd list",odd)
