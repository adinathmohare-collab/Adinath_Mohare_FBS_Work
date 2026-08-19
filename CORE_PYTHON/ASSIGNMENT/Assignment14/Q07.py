# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa. Use the Python set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1)
print(set2)
print('Missing no in set 1 which are present in set2',set2.difference(set1))
print('Missing no in set 2 which are present in set1',set1.difference(set2))
