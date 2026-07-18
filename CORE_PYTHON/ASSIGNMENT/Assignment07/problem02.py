# print


#    *
#    **
#    ***
#    ****
#    *****
#    ****
#    ***
#    **
#    *

for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()