# 1. Python Program to Add a Key-Value Pair to the Dictionary

student = {
    "name": "Saurabh",
    "age": 21,
    "city": "Pune"
}
print('Original dictionary: ',student)
key = input("Enter key to add to dictionary: ")
value = input("Enter value to add to dictionary: ")
student[key] = value
print(f'Updated dictionary: {student}')