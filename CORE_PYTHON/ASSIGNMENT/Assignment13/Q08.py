# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

string =  input("Enter string to count occurence of word using dictionary: ") 

words=string.split()

dictionary={}

for i in words:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1

print(dictionary)
