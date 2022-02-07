import sys

lines = [ line.strip() for line in sys.stdin]

N = int(lines[0])

for i in range(N):
   print(lines[N-i])



