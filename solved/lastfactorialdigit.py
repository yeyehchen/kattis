import sys

lines  = [line.strip() for line in sys.stdin]
T = int(lines[0])
lisN = []
for i in range(T):
    num = int(lines[i+1])
    lisN.append(num)

for num in lisN:
    total = 1
    for x in range(num):
        total *= (x+1) 
    end = str(total)
    final = end[-1]
    print(final)
