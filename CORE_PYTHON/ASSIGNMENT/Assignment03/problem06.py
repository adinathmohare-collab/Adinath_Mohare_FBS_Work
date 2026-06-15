#6. Write a program to calculate profit or loss.

cp=int(input("Enter cost price:"))
sp=int(input("Enter selling price"))

if(sp>cp):
    print("profit")
elif(sp<cp):
    print("Loss")
else:
    print("No profit no loss")