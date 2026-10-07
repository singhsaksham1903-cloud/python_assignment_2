import re
text = input("enter the String: ")
words = re.findall(r"[A-Z][a-z]+",text)
print(words)


