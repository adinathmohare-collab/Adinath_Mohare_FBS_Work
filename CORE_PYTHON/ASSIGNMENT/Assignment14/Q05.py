# 5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

strings = ["flower", "flow", "flight",'flyover']

smallest = min(strings,key=len)
prefix  = ""

for i in range(len(smallest)):
    chars = set()
    for word in strings:
        chars.add(word[i])

    if len(chars)==1:
        prefix+=smallest[i]
    else:
        break
if prefix == '':
    print('Words are not same')
else:
    print('Largest common prefix:',prefix)