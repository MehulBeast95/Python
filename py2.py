"""temp = 34
if 40 >= temp >= 20:
    print("Very hot")
    print("take fluids")
elif temp <= 35 or temp >= 20:
    print("moderate today")

elif not temp ==20:
    print("Can be predicted")
else:
    print("i need to be there")"""
#wap weight convertor in python
"""while True:
    print("1) Kg to Pounds \n2) Pounds to Kg \n3)Exit")
    a=int(input("Enter choice: "))
    if a==1:
        b=float(input("Enter weight in Kg:"))
        c=b*2.2
        print("Your weight in Pounds is:",c)
    elif a==2:
        d=float(input("Enter weight in Pounds:"))
        e=d/2.2
        print("Your weight in Kg is:",e)
    else:
        print("Thank you")
        break


print("Kg will be converted to Lbs and Lbs into Kg")
a = float(input("Enter weight: "))
b = input("Enter unit: ")
if b.lower() == "kgs" or "kg":
    c=a*2.20
    print("Your weight in lbs is: ",c)
elif b.lower() == "lbs" or "lb":
    d=a/2.20
    print("Your weight in Kgs is: ",d)"""

#wap on car automation
while True:
    print("1)Start \n2)Stop \n3)Help \n4)Quit")
    a=int(input("Enter Choice: "))
    if a == 1:
        print("The car has started")
    elif a == 2:
        print("The car has stopped")
    elif a == 3:
        print("Start --> The car has started \nStop --> The car has stopped \nQuit -->Quit the game")
    elif a == 4:
        print("Thank you")
        break
