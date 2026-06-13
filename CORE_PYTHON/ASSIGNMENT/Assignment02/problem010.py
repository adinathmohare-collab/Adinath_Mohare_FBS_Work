#10. Write a program to reverse three-digit number.
num=int(input("Enter the number:"))

d1=num % 10 
num=num // 10

d2=num % 10
num=num // 10

d3=num % 10
num // 10

R=d1*100+d2*10+d3
# d1*100 to take digit hundred place.
# d2*10 to take digit tenth place.
# d3    just need to add. it goes automatically unit place.

print("Reverse no is::",R)