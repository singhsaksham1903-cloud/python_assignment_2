import re

ip = input("Enter an IP address: ")

pattern = re.match(r"^\d{1,3}(\.\d{1,3}){3}$",ip)



if pattern:
    print("Valid IP address:", pattern.group())
else:
    print("Invalid IP address")  # Print a message indicating the IP address is invalid