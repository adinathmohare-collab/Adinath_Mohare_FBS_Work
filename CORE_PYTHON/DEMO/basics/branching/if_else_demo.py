# find positive or negative value using if else:-
n1=int(input("Enter the value positive or negative:"))
if(n1>0):
    print(n1,"is positive.")# 0 is exeption for now
else:
    print(n1,"is negative.")

# Find entered number even or odd:-
n2=int(input("Enter the number for check even or odd:"))
if(n2%2 == 0):
    print(n2,"is even.")
else:
    print(n2,"is odd")
    
#Enter valid id and password for logged in,id or password wrong then logged in failed:-
uid=input("Enter valid id:")
pas=int(input("Enter valid pin no.:"))
valid_id="ganesh"
valid_pass=1312
if(valid_id==uid and valid_pass==pas):
    print("logged in successful!")
    
else:
    print("logged in failed!")
