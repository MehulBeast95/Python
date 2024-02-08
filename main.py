stk = []


def push():
    while True:
        x = input("Enter name: ")
        stk.append(x)
        display()
        ch = input("Enter more ? :  ")
        if ch == "no":
            break


def pop():
    if not stk:
        print("Underflow")
    else:
        z = stk.pop()
        print("deleted element: ", z)
        display()


def display():
    a = len(stk - 1)
    for i in range(a - 1, -1, -1):
        print(stk[i])


while True:
    print("1.Add\n2.Delete \n3.Display \n4.Exit \n")
    c = int(input("Enter choice(1-4): "))
    if c == 1:
        push()
    elif c == 2:
        pop()
    elif c == 3:
        display()
    else:
        break