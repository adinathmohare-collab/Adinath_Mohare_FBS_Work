# 10. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions 

string1 = input("Enter first string to find largest string: ")
string2 = input("Enter second string to find largest string: ")

count1 = 0
count2 = 0
for i in string1:
    count1+=1
for i in string2:
    count2+=1
if count1>count2:
    print(f'Largest string:{string1}')
elif count2>count1:
    print(f'Largest string:{string2}')
else:
    print("Both strings are equal")