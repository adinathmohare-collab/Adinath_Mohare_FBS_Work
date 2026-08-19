# 2. Python Program to Concatenate Two Dictionaries Into One

student = {
    "name": "Saurabh",
    "age": 21,
    "city": "Pune"
}

Marks = {
    'Java': 90,
    'Python': 95,
    'SQL': 90
}

print(f'Dictionary 1:{student}')
print(f'Dictionary 2:{Marks}')
student.update(Marks)
print(f'Concatenated dictionary:{student}')