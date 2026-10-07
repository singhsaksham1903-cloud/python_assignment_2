import re
text = input("Enter a string: ") # Enter the string to split
result = re.split(r" and ", text) # Split the string using " and " as the delimiter
print(result)  # Print the resulting list of substrings