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