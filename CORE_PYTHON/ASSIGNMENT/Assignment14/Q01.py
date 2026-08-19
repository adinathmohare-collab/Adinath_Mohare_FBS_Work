# 1. Write a Python program to find elements in a given set that are not in another set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(f'Set 1: {set1}')
print(f'Set 2: {set2}')
print(f'Elements which are not in set2 but present in set1: {set1.difference(set2)}')