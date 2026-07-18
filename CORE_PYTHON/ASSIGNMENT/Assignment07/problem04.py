# print

#            1
#          2 3 2
#        3 4 5 4 3
#      4 5 6 7 6 5 4
#    5 6 7 8 9 8 7 6 5

for i in range(1,6):

    for j in range(6-i):
        print(" ",end=" ")

    n=i

    for j in range(i):
        print(n,end=" ")
        n+=1

    n-=2
    for j in range(i-1):
        print(n,end=" ")
        n-=1   
    print()