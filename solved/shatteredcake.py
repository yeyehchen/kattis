import sys

lines = [line.strip() for line in sys.stdin]

W = int(lines[0])
N = int(lines[1])
a = 0
for i in range(N):
    p = lines[i+2].split()
    a += int(p[0]) * int(p[1])
print(int(a/W))
