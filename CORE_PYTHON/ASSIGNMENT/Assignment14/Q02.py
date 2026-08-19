# 2. Write a Python program to remove the intersection of a second set with a first set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}

print(f'Set 1: {set1}')
print(f'Set 2: {set2}')

set1.difference_update(set2)    #This removes all elements from set1 that are also present in set2.
print(f'Set after removing intersection: {set1}')