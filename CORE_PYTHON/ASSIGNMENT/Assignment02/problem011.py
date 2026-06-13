#11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

#Take input from user               
A=int(input("Enter the Amount:"))

#Perform oprations
N500 = A // 500
A=A % 500

N100 = A // 100
A=A % 100

N50 = A // 50
A=A % 50

N20 = A // 20
A=A % 20

N10 = A // 10
A=A % 10

N5 = A // 5
A=A % 5

N2 = A // 2
A=A % 2

N1 = A // 1
A=A % 1

#Display output.
print(" Notes of 500::",N500)
print("Notes of 100::",N100)
print("Notes of 50::",N50)
print("Notes of 20::",N20)
print("Notes of 10::",N10)
print("Notes of 5::",N5)
print("Notes of 2::",N2)
print("Notes of 1::",N1)