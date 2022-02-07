import sys
import math

lines = [line.strip() for line in sys.stdin ]

first_line = lines[0].split()
N = int(first_line[0])
W = int(first_line[1])
H = int(first_line[2])

longest = math.sqrt(W*W + H*H)

for i in range(1,N+1):
    x = int(lines[i])
    if x <= longest:
        print("DA")
    else:
        print("NE")    
