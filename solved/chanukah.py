import sys

lines = [line.strip() for line in sys.stdin]

P = int(lines[0])


for i in range(P):
    i = i + 1
    line = lines[i].split()
    D = int(line[1])
    sum = 0
    for x in range(D + 1):
        sum += x
        total = sum + D
    print(i,total)