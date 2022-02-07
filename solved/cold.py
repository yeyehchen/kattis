import sys

lines = [line.strip() for line in sys.stdin]

line = lines[1].split()
n = int(lines[0])
count = 0 
for i in range(n):
    if int(line[i]) < 0:
        count += 1
print(count)    
