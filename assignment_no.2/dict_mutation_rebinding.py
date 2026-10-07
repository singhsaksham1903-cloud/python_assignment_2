def add_entry(d):
    d["age"] = 20


def reassign_dict(d):
    d = {"name": "Rahul", "age": 25}
    print("Inside reassign_dict():", d)


# Taking input from user
name = input("Enter your name: ")

my_dict = {"name": name}

print("Before function calls:", my_dict)

# Function 1
add_entry(my_dict)
print("After add_entry():", my_dict)

# Function 2
reassign_dict(my_dict)
print("After reassign_dict():", my_dict)