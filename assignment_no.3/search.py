import re # Import the regular expression module
text = input("enter the String: ") # Enter the string to search for digits
m = re.search(r"\d+",text) # Search for the first occurrence of digits in the string
print(m.group()) # Print the first occurrence of digits in the string
print("the starting index of the digit is: ",m.start()) # Print the starting index of the first occurrence of digits in the string
print("and the end index of the digit is: ",m.end()) # Print the end index of the first occurrence of digits in the string


