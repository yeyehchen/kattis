import sys

def withAdOrNot(r, e, c):
    if r > e - c:
        print("do not advertise")
    elif r == e - c:
        print("does not matter")
    else: 
        print("advertise")  

lines = [line for line in sys.stdin]

n = int(lines[0])

for i in range(n):
    data = lines[i + 1].split()
    r = int(data[0])
    e = int(data[1])
    c = int(data[2])
    withAdOrNot(r, e, c)