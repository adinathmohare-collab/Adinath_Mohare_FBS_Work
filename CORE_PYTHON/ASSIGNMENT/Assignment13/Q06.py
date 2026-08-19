# 6. Python Program to Multiply All the Items in a Dictionary 

marks = {
    "Java": 90,
    "Python": 95,
    "SQL": 85
}

product=1
for value in marks.values():
    product*=value

print(f'dictionary: {marks}')
print(f'product of values in dictionary:{product}')