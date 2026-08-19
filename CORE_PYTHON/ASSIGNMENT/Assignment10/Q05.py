# 5. Accept a number from user and check if this element is present in the list or not.
#  Also tell how many times it is present in the list.

def searchelement(n,li):
    count = 0
    for i in li:
        if i == n:
            count += 1
    if n in li:
        print(f'{n} is present in list {count} times')
    else:
        print(f'{n} is not present in list')


n = int(input("Enter no to check element is present in list or not: "))
li = [2,8,33,9,5,2,9,2,11]
searchelement(n,li)

