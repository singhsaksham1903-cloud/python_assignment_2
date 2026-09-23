def change_string(s):
    s = "X" + s[1:]
    print("Inside function:", s)


s = input("Enter a string: ")

print("Before function call:", s)

change_string(s)

print("After function call:", s)