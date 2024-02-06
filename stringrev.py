#wap to reverse a given string without using inbuilt functions
s=input("Enter string: ")
"""print(s[::-1])"""
a=""
for i in s:
    a=i+a
print(a)