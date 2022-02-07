import sys

lines = [line.strip() for line in sys.stdin]

N = int(lines[0])

newN = int(N/2)
nl = [N%2]
while newN >= 1:
    num = newN %2
    newN = int(newN/2)
    nl.append(num)
x = len(nl)
reverse = []   
for i in range(x):
    print(nl[x-(i+1)])    



