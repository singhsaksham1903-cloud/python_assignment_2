import re
text = input("enter the String: ")
nums = re.findall(r"\d+",text)
print(nums)


