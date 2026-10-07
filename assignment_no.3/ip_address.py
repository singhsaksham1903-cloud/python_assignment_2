import re

ip = input("Enter an IP address: ")

pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

m = re.match(pattern, ip)

if m:
    print("Valid IP address:", m.group())
else:
    print("Invalid IP address")  # Print a message indicating the IP address is invalid