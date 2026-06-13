# Write a program to calculate selling price of book based on cost price and discount.

#Take input from user
CP=float(input("Enter the price of book"))
Discount=float(input("Enter the discount:"))

#Perform operations
DA=CP*Discount/100
SP=CP-DA

#Display output
print("Discount Amount is::",DA)
print("Selling Amount is::",SP)