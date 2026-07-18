# Q:- Write a program to display following program.

# 1
# 2 3
# 4 5 6
# 7 8 9 10

num = 0
for i in range (1,6):
    for j in range (1,i):
        num= num+1
        print(num,end=" ")
    print()