# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

key = input("Enter key to search: ")

student = {
    "name": "Saurabh",
    "age": 21,
    "city": "Pune"
}

for i in student :
    if i == key:
        print(f"{key} found in dictionary")
        break
else:
    print(f'{key} does not exist in dictionary')








