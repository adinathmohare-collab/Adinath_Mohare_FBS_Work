# 13.  Python Program to count number of digits and letters in a string. 

string = input('Enter string to count no of digits and letters in string: ')
digit=0
letter=0
for i in string:
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            letter+=1
        else:
            pass
print(f'No of digit:{digit}\nNo of letters:{letter}')