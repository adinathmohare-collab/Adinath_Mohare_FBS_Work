# 8. Print 1 to 100 in snakes and ladder pattern. 

num = 1

for row in range(10):
    if row % 2 == 0:
        for col in range(10):
            print(num, end="\t")
            num += 1
    else:
        temp = num + 9
        for col in range(10):
            print(temp, end="\t")
            temp -= 1
        num += 10

    print()