'''def fact(n):
    if n == 0 or n == 1:
        print(1)
    else:
        c = 1
        for i in range(2, n + 1):
            c = c * i
        print(c)
        fact()
fact()'''
""""################################
n = int(input("Enter a number: "))
k=1
for i in range(2,n):
    k = n%i
    if k == 0:
        print(n, "is not a prime number")
        break
if k!=0:
    print(n, "is a Prime number")"""
###############################
#waf to generate fibonacci series
def fibo(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fibo(a-1) + fibo(a - 2)
print(fibo(12))