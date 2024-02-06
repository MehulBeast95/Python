# wap to write a function that does the arithmetic operation
def add(x, y):
    z = x + y
    print(z)


def subtract(x, y):
    z = x - y
    print(z)


def divide(x, y):
    z = x / y
    print(z)


def multiply(x, y):
    z = x * y
    print(z)


while True:
    print("1)ADD \n2)SUBTRACT \n3)DIVIDE \n4)MULTIPLY \n5)EXIT")
    x = int(input("Enter x: "))
    y = int(input("Enter y:"))
    a = int(input("Enter choice: "))
    if a == 1:
        add(x, y)
    elif a == 2:
        subtract(x, y)
    elif a == 3:
        divide(x, y)
    elif a == 4:
        multiply(x, y)
    elif a == 5:
        break