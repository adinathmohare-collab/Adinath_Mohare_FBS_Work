#2. Write a program to input any alphabet and check whether it is vowel or consonant. 

#Take input from user
a=(input("Enter the any alphabets:"))

#perform operation
if(a in "aeiouAEIOU"):
    print(" It's vowel")
else:
    print("It's consonant")