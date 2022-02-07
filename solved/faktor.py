import sys

lines = [line for line in sys.stdin]

num = lines[0].split()

A = float(num[0])
I = float(num[1])
X = A * (I - 0.99)

if X - int(X) != 0 :
    X += 1
print(int(X))