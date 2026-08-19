# 7. Python Program to Remove the Given Key from a Dictionary

marks = {
    "Java": 90,
    "Python": 95,
    "SQL": 85
}

print(marks)
key = input("Enter key to remove from above dictionary: ")
if key in marks.keys():
    del marks[key]
    print(marks)
else:
    print('Key not found')


