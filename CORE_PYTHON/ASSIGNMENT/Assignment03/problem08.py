#8. Write a program to prompt user to enter userid and password. After verifying 
    #userid and password display a 4 digit random number and ask user to enter the 
    #same. If user enters the same number then show him success message otherwise 
    #failed. (Something like captcha) 

import random
Id="pratikg"
passw=1234

a=input("Enter the user_id:")
b=int(input("Enter 4 digit password:"))
c=random.randint(1000,9999)

if(a==Id and b==passw):
    print("UID and password is correct")
    print("captcha:-",c)
    ca=int(input("Enter the captcha:"))

    if(ca==c):
        print("login successfully")
    else:
        print("incorrect captcha")
else:
    if(a!=Id):
        print("Invalid user name")
    elif(b!=passw):
        print("Invalid password")
    else:
        print("Invalid user id or password")  