#  Write a program to display given pattern.

#    A
#    A B
#    A B C
#    A B C D
#    A B C D E
m=65
for i in range(1,6):
    m=65
    for j in range(1,i+1):
        print(chr(m),end=" ")
        m +=1
    print()
