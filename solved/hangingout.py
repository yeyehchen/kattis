import sys

lines = [line.strip() for line in sys.stdin]

line = lines[0].split()
L = int(line[0])
X = int(line[1])
events = lines[1:X+1]

total = 0
notallow = 0
for event in events:
    each = event.split(" ")

    if each[0] == "enter":
        if total + int(each[1]) > L:
            total += 0
            notallow += 1     
        else:
            total += int(each[1])    

    elif each[0] == "leave":
        total -= int(each[1])
     
print(notallow)
             
 
    
