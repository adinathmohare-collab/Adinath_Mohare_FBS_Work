# 5. Python Program to Sum All the Items in a Dictionary

marks = {
    "Java": 90,
    "Python": 95,
    "SQL": 85
}

total=0
for value in marks.values():
    total+=value

print(f'dictionary: {marks}')
print(f'Sum of values in dictionary:{total}')