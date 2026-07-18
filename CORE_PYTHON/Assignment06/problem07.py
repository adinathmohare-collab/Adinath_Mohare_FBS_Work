# Write a program to display the given pattern.

#            A 
#          A B C
#        A B C D E
#      A B C D E F G
#    A B C D E F G H I
m=65
for i in range(1,6):
    for j in range(6-i,1,-1):
        print(" ",end=" ")
    for j in range(i*2-1):
        print(chr(m+j),end=" ")
    print()