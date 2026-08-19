# 3. Python Program to Detect if Two Strings are Anagrams


string1 = input("Enter 1st string to check Anagram or not: ").lower()
string2 = input("Enter 2nd string to check Anagram or not: ").lower()

if len(string1) != len(string2):
    print("String is not Anagram")
else:
    if  sorted(string1) == sorted(string2):
        print("String is Anagram")
    else:
        print("String is not Anagram")

  
