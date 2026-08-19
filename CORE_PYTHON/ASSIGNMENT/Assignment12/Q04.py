# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string = 'Good Night'
exchanged = string[-1]+string[1:-1]+string[0]
print(f'Originial String:{string}')
print(f'String after exchanging first and last character:{exchanged}')
