# 7. Python Program to Calculate the Length of a String Without Using a Library Function

string = input("Enter string to count length: ")
len=0
for i in string:
    len+=1
print(f'Length of given string is: {len}')