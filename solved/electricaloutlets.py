import sys

lines = [line.strip() for line in sys.stdin]

N = int(lines[0])

for i in range(N):
    line = (lines[i+1]).split()
    K = int(line[0])
    test = line[1:]
    total = 0   
    for num in test:
        total += int(num)
    p = total - K + 1
    print(p)     

                          