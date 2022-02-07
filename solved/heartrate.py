import sys

lines = [line.strip() for line in sys.stdin]

N = int(lines[0])

for i in range(N):
    line = lines[i + 1].split()
    b = int(line[0])
    p = float(line[1])
    BPM = b * 60 / p 
    maxt = p / (b - 1)
    mint = p / (b + 1)
    print(60/maxt, BPM, 60/mint)
  
    