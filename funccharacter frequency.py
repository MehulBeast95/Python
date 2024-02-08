#wap to calculate the character frequency
a=input("Enter word: ")
l = {}
for i in a:
    if i in l:
        l[i] += 1
    else:
        l[i] = 1
print("frequency of character in ",a ,"is : "+ str(l))