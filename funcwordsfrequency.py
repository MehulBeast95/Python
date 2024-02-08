#wap to calculate the frquency of words in a sentence
def fre(a):
    a=a.split()
    l=[]
    for i in a:
        if i not in l:
            l.append(i)
    for i in range(0, len(l)):
        print(" frequency  of", l[i], ": ", a.count(l[i]))
a=input("Enter string: ")
fre(a)
#wap to calculate the character frequency
a=input("Enter word: ")
l = {}
for i in a:
    if i in l:
        l[i] += 1
    else:
        l[i] = 1
print("frequency of character in ",a ,"is : "+ str(l))