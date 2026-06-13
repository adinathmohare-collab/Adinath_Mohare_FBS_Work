#6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

s=int(input("Enter the salary"))

da=s*10/100
ta=s*12/100
hra=s*15/100
T=da+ta+hra

print("Toatl salary is::",T)

