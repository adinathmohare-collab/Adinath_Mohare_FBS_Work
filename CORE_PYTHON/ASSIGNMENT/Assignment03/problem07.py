#7. Write a program to check if user has entered correct userid and password. 

Id="pratikg"
passw=1234

a=input("Enter the user_id:")
b=int(input("Enter 4 digit password:"))

if(a==Id and b==passw):
    print("Login successfully")
else:
    if(a!=Id):
        print("Invalid user name")
    elif(b!=passw):
        print("Invalid password")
    else:
        print("Invalid user id or password")