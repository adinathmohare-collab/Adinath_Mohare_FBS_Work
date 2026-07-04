 # WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
 
st = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Numbers divisible by 7 and multiple of 5:")

for i in range(st , end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")