import re
text = input("enter the string: ")
word = input("enter the word to search: ")
print(re.findall(rf"{word}", text, re.I))
print("Number of occurrences:", len(re.findall(rf"{word}", text, re.I)))