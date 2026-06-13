#3. Convert distant given in feet and inches into meter and centimeter.

#Take input from user

f=float(input("Enter the feet:"))
i=float(input("Enter the inches:"))

#Perform operations

T=(f*12)+i          # 1 feet=12 inches
M=T // 100
Cm=T % 100

#Display Output
print("Total inches is::",T)
print("Meter is:",M)
print("Centimeter is :",Cm)