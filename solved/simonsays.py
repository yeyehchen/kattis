import sys

lines = [ line.strip() for line in sys.stdin]
N = int(lines[0])

for i in range(N):
    senten = lines[i+1].split()
    if senten[:2] == ["Simon", "says"]:
        x = ' '.join(senten[2:])
        print(x)