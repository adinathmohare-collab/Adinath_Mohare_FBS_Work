# 2. Python Program to Remove the nth Index Character from a Non-Empty String

string = input("Enter string: ")
new = ''
n = int(input("Enter index to remove character from entered string :"))

for i in range(len(string)):
    if i == n:
        continue
    else:
        new += string[i]
    
print(new)
