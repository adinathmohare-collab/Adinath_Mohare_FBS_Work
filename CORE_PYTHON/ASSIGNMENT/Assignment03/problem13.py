# 13. Write a program to input electricity unit charges and calculate total electricity bill 
    # according to the given condition: 
    # For first 50 units Rs. 0.50/unit 
    # For next 100 units Rs. 0.75/unit 
    # For next 100 units Rs. 1.20/unit 
    # For unit above 250 Rs. 1.50/unit 
    # An additional surcharge of 20% is added to the bill 

u=int(input("Enter total units"))

if(u<=50):
    t=u*0.50
elif(u<=150):
    t=(50*0.50)+((u-50)*0.75)
elif(u<=250):
    t=(50*0.50)+(0.75*100)+((u-150)*1.20)
else:
    t=(50*0.50)+(0.75*100)+(1.20*100)+((u-250)*1.50)
    t=t+(t*20/100)
    print("Total Bill:",t)