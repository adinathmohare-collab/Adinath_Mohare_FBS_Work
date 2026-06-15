#11. Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 

p1=int(input("Enter the person 1 age:"))
T=100
if(p1<=12):
    da=T*30/100
    p1=T-da
    print("Discount Amount is",p1)
    print("Child")
elif(p1>=59):
    da=T*50/100
    p1=T-da
    print("Discount Amount is",p1)
    print("senior citizon")
else:
    print("other need to pay full ")
    p1+=T
    print(p1)


p2=int(input("Enter the person 2 age"))
T=100
if(p2<=12):
    da=T*70/100
    p2=T-da
    print("Discount Amount is",p2)
    print("Child")
elif(p2>=59):
    da=T*50/100
    p2=T-da
    print("Discount Amount is",p2)
    print("senior citizon")
else:
    print("other need to pay full ")
    p2=T



p3=int(input("Enter the person 3 age:"))
T=100
if(p3<=12):
    da=T*30/100
    p3=T-da
    print("Discount Amount is",p3)
    print("Child")
elif(p3>=59):
    da=T*50/100
    p3=T-da
    print("Discount Amount is",p3)
    print("senior citizon")
else:
    print("other need to pay full ")
    p3=T


p4=int(input("Enter the person 4 age:"))
if(p4<=12):
    da=T*30/100
    p4=T-da
    print("Discount Amount is",p4)
    print("Child")
elif(p4>=59):
    da=T*50/100
    p4=T-da
    print("Discount Amount is",p4)
    print("senior citizon")
else:
    print("other need to pay full ")
    p4=T


p5=int(input("Enter the person 5 age:"))
if(p5<=12):
    da=T*30/100
    p5=T-da
    print("Discount Amount is",p5)
    print("Child")
elif(p5>=59):
    da=T*50/100
    p5=T-da
    print("Discount Amount is",p5)
    print("senior citizon")
else:
    print("other need to pay full ")
    p5=T

Total=p1+p2+p3+p4+p5
print("Total Amount of 5 persons is::",Total)
