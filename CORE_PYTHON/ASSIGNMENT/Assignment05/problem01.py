# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
# t=3
id="admin123"
pas="321"
n=3
for i in range(0,n):
    print(f'You have {n} chances to enter correct userid and password: ')
    userid=input("Enter userid: ")
    password=input("Enter password:")
    if userid==id and pas==password:
        print("Login sucessful! ")
        break
    else:
        print("Enter correct credentials! ")
    n-=1
    
