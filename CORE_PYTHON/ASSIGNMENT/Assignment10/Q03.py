# 3. Write a program to find the second largest element in the list. 

def sec_largest(li):
    maximum = li[0]
    second = li[0]
    for i in li:
        if i > maximum:
            second = maximum 
            maximum = i
        elif i>second and i!=maximum:
            secon = i
    return maximum,second

li = [10,30,40,60,20,20,90]
Max,Min = sec_largest(li)
print("Largest elelemt is:",Max)
print("second largest element is:",Min)