import sys

lines = [ line.strip() for line in sys.stdin ]
n = int(lines[0])

for i in range(n):
    group = lines[i+1].split(" ")
    a = int(group[0])
    b = int(group[1])
    c = int(group[2])
    if a + b == c or a + c == b or c + b == a :
        print("Possible")
        continue
    elif a / b == c or a / c == b or c / b == a :
        print("Possible")
        continue  
    elif a - b == c or a - c == b or c - b == a :
        print("Possible")
        continue   
    elif a * b == c or a * c == b or c * b == a :
        print("Possible")
        continue   
    else:
        print("Impossible")
        continue              
