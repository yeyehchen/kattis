import sys

lines = [line for line in sys.stdin]

x = lines[0].split()

r1 = int(x[0])
s = int(x[1])

r2 = s*2 - r1
print(r2)
