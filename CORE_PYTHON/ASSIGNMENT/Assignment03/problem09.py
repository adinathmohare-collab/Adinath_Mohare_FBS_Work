#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

S1=int(input("Enter the sub 1 mark:"))
S2=int(input("Enter the sub 2 mark:"))
S3=int(input("Enter the sub 3 mark:"))
S4=int(input("Enter the sub 4 mark:"))
S5=int(input("Enter the sub 5 mark:"))

T=((S1+S2+S3+S4+S5)/500)*100
print(T)

if(T>=90):
    print("first class")
elif(T>=60):
    print("Second class")
elif(T>35):
    print("Third class")
else:
    print("Failed")