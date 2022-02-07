import sys

lines = [line.strip() for line in sys.stdin]

line = lines[0].split()

N = int(line[0])
M = int(line[1])

if N == M :
    x = N + 1
    print(x)
elif N > M :
    for i in range(N-M+1):
        i = i + 1
        x = M + i
        print(x)
elif M > N :
    for i in range(M-N+1):
        i = i + 1
        x = N + i
        print(x)