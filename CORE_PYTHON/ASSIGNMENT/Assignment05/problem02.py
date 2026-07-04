# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
n=int(input("Enter no of strudents: "))
per=0
for i in range(1,n+1):
    print(f'Enter 5 subject marks of no {i} student ')
    t=0
    for j in range(1,6):
        m=(int(input(f'Enter marks of no {j} subject marks: ')))
        t+=m
    percentage=t/500*100
    per+=percentage
    print("Percentage: ",percentage)
avg_percentage=(per/(n))
print("Average percentage of students: ",avg_percentage)