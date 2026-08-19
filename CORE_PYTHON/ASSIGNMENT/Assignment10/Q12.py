# 12 . Write a program to create three lists of numbers, their squares and cubes 


def square_cube(li,square,cube):
    for i in range(len(li)):
        square.append(li[i]**2)
        cube.append(li[i]**3)

li = [1,2,3,4,5,6,7]
square = []
cube = []
square_cube(li,square,cube)
print("Original list: ",li)
print("Square of list: ",square)
print("cube of list: ",cube)