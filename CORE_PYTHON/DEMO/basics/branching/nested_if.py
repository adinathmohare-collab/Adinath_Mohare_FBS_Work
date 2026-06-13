#gender, and age criteria for marrage
gender=str(input("Enter your gender:"))
age=int(input("Enter your age:"))
if(gender=="male"):
    if(age>=21):
        print("eligible for marrige")
    if(age<=21):
        print("not elible for marrige")
if(gender=="female"):
    if(age>=18):
        print("eligible for marrige")
    if(age<=18):
        print("not elible for marrige")
