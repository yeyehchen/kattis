import sys

lines = [line.strip() for line in sys.stdin]

C = float(lines[0])
L = int(lines[1])
total = 0

for i in range(L):
    line = lines[i + 2].split()
    w = float(line[0])
    l = float(line[1])
    total += w * l
print(round(C * total, 7))    

