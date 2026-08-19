# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String 

string = input("Enter string to count no of characters and no of words : ")
words = string.split()

print(f'No of characters in string: {len(string)} \nNo of words: {len(words)}')
