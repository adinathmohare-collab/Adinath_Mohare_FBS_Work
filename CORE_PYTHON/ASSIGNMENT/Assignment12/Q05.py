# 5. Python Program to Count the Number of Vowels in a String 

string = input("Enter string to count vowels in string: ").lower()
vowels=0
for i in string:
    if i in 'aeiou':
        vowels+=1
print(f'No of vowels:{vowels}')
