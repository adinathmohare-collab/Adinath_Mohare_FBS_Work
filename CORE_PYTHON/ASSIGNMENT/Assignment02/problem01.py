#1. Convert the time entered in hh,min and sec into seconds.

#Take input from user

H=int(input("Enter the Hours:"))
M=int(input("Enter the Minutes:"))
S=int(input("Enter the seconds"))

#Perform operations

Total_sec=H*3600+M*60+S

#Display output
print("Total Second is:",Total_sec)

