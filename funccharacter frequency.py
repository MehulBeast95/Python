#wap to calculate the character frequency
def freq(a):
    d={}
    for keys in a.lower():
        d[keys] = d.get(keys, 0) + 1
    print("Count of all characters in ",a," is : \n"+ str(d))
a=input("Enter word: ")
freq(a)