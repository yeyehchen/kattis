import sys

lines = [line.strip() for line in sys.stdin]

n = int(lines[0])
bats = lines[1].split()
total = 0

for i in range(n):
    if int(bats[i]) == -1:
        bats[i] = 0
        n -= 1
    total += int(bats[i])
    slug = total/n

print(slug)

        
