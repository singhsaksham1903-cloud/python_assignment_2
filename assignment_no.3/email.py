import re

text = input("Enter a email: ")

email = re.match(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", text)

if email:
    print("It is an email:", email.group())
else:
    print("Not a valid email")