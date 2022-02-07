import sys

lines = [line for line in sys.stdin]

N = int(lines[0])

q = []
y = []

for i in range(N):
    data = lines[i + 1].split()
    q.append(float(data[0]))
    y.append(float(data[1]))
    
def solve(N, q, y):
    qaly = 0
    for i in range(N):
        qaly += q[i] * y[i]
    print(qaly)

solve(N, q, y)
