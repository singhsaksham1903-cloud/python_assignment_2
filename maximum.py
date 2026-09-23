def maximum(a,b):
    if a > b:
        return a
    else:
        return b

num_1 = int(input("Enter the first Number: "))
num_2 = int(input("enter the second Number: "))
result = maximum(num_1,num_2)
print("the maximum number between", num_1, "and", num_2, "is", result)
