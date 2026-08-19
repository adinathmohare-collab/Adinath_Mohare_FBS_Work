# 12.  Python Program to count number of lowercase characters in a string. 

string = input("Enter string to count lowercase characters: ")
lower=0
for i in string:
    if i.islower():
        lower+=1

print(f'total lowercase characters in string:{lower}')