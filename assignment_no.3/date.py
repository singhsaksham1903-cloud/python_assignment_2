import re

text = input("Enter a date: ")

date = re.match(r"^\d{2}-\d{2}-\d{4}$", text)


if date:
    print("It is a date:", date.group())
else:
    print("Neither a valid date")