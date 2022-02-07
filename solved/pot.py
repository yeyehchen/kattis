import sys

lines = [line for line in sys.stdin]

N = int(lines[0])
x = 0

for i in range(N):
    n = int(lines[i + 1])
    p = n%10
    n = n//10
    x += n ** p
print(x)


  
