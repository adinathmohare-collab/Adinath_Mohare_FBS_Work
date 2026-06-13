# Problem 5:-
# Write a program to enter P,T,R and calculate compound interest:-

p=float(input("enter initial amount:-"))
r=float(input("enter the rate of interest:-"))
t=float(input("enter the time (in years):-"))
a=p*(1+r/100)**t  #Final amount
ci=a-p
print("Compound interest is:-",ci)
