import re
text = input("Enter a string: ") # Enter the string to substitute
word = input("Enter the word to substitute: ") # Enter the word to substitute
replacement = input("Enter the replacement word: ") # Enter the replacement word
new_text = re.sub(rf"{word}", replacement, text) # Substitute the word in the string with the replacement word
print(new_text)  # Print the resulting string after substitution