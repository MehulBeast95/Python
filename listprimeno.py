#WAP to create a list of prime no from 1 to 100
l1 = []
for i in range(2, 100):
    a = True
    for x in range(2, i):
        if i % x == 0:
            a = False
    if a:
        l1.append(i)
print(l1)
