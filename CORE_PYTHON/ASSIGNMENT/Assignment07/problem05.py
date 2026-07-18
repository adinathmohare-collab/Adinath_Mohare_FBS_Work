# print

#             1 
#           1   2
#         1       3
#       1           4
#     1  2  3  4  5  6

for i in range(1,6):
    for j in range(6-i):
        print(" ",end=" ")
    if i==5:
        for j in range(1,6+1):
            print(j ,end="  ")
    else:
        print(1,end=" ")
        for j in range(1,2*i-2):
            print(" ",end=" ")
        if i>1:
            print(i,end=" ")

    print()