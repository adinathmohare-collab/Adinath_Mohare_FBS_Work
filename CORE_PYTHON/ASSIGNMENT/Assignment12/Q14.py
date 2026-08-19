# 14.  Python Program to count the occurrences of each word in a string.

string = input("Enter the string to count occurrence of each word: ")
printed = []
words = string.split()
for i in words:
    if i not in printed:
        print(i,words.count(i))
        printed.append(i)
