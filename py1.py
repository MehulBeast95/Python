"""z = int(input("Enter First no: \n"))
x = int(input("Enter Next no: \n"))
a = z + x
b = z - x
c = z * x
d = z % x
e = z // x
f = z / x
g = z ** x
h = z == x
i = x >> 2
j = z & x
k = z | x
l = z << 2
print(z == x)
print(z != x)
print(z >= x)
print(z <= x)
print(z > x)
print(z < x)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
m = True
n = False
print(m and n)
print(m is not n)
print(not n)
print(not m)
print(m or n)
"""
l1 = []
for i in range(2, 100):

    # Assume number is prime until shown it is not.
    a = True
    for x in range(2, i):
        if i % x == 0:
            a = False

    if a:
        l1.append(i)
print(l1)
