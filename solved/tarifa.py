import sys

lines = [line.strip() for line in sys.stdin]

X = int(lines[0])
N = int(lines[1])
spend = X * (N+1) 
for i in range(N):
    spend -= int(lines[i+2])    
print(spend)     
