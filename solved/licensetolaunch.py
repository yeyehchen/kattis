import sys

lines = [line.strip() for line in sys.stdin]

n = int(lines[0])
lis = [int(t) for t in lines[1].split()]
answer = lis.index(min(lis))
print(answer)