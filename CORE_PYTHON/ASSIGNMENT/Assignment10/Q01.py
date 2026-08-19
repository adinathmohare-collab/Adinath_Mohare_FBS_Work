# 1. Write a program to find sum of all elements of list

def sum_of_list_elements(li):
    sum = 0
    for i in li:
        sum += i
    print("Sum =",sum)

li = [50, 40, 30, 20, 10]
sum_of_list_elements(li)