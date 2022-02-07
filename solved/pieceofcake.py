import sys

lines = [line for line in sys.stdin]

x = lines[0].split()

n = int(x[0])
h = int(x[1])
v = int(x[2])

A = v * h * 4
B = (n - h) * v * 4
C = (n - v) * h * 4
D = (n - v) * (n - h) * 4

biggest = max(A, B, C, D)

print(biggest)

      