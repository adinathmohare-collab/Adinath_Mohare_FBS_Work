## Problem 8:-
#write a program to convert days into years,weeks and days.
tdays=int(input("Enter days:")) #total days
y=tdays // 365 #years
print("Total years:",y)
rdays=tdays%365 #remaining days

w=rdays // 7
days=rdays % 7
print("Weeks:",w)
print("days:",days)

