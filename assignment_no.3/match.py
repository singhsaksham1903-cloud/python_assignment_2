import re # Import the regular expression module

text = input("Enter a string: ") # Enter the string to match
word = input("Enter the word to match: ") # Enter the word to match against the string

m = re.match(rf"{word}", text) # Match the word at the beginning of the string

if m:  # Check if a match was found
    print("Match found:", m.group())  # Print the matched word
else:
    # No match found at the beginning of the string
    print("No match found")  # Print a message indicating no match was found