#wap to remove duplicates and sort them in ascending order
l1=[5,2,2,2,3,4,3,5,4,2,3,6,7,5,6,7]
a=[]
for i in l1:
    if i not in a:
        a.append(i)
        a.sort()
print(l1)
print(a)