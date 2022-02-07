import sys

lines = [ line.strip() for line in sys.stdin]
line = lines[0].split()

h = int(line[0]) * 60 
m = int(line[1])
n = h + m - 45

newn = int(n /60)
newh = n%60

if newn == 0:
    newn = 23
    
print(newn , newh)
