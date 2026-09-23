def remove_last(lst):
    lst.pop()

num=[]
a=int(input("enter the integers in the list: "))
for i in range(a):
    num.append(int(input(f"enter element {i+1}: ")))

print("Before function call:", num)

remove_last(num)

print("After function call:", num)