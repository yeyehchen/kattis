import sys

lines = [line.strip() for line in sys.stdin]

x = lines[0]
cups = ["ball", "no1", "no2"]

for i in range(len(x)):
    order = []
    if x[i] == "A":
        order.append(cups[1])
        order.append(cups[0])
        order.append(cups[2])
        cups = order
    elif x[i] == "B":
        order.append(cups[0])
        order.append(cups[2])
        order.append(cups[1])
        cups = order
    elif x[i] == "C":
        order.append(cups[2])
        order.append(cups[1])
        order.append(cups[0])
        cups = order      
    postion = cups
print(postion.index('ball')+1)     

