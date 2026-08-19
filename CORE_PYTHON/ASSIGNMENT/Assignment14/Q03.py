# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set data type.

strings = [
    "apple mango",
    "mango banana",
    "apple orange"
]

words = []
for sentense in strings:
    words.extend(sentense.split())

unique=set(words)
for word in unique:
   count = words.count(word)
   print(f' {word}:{count}')


