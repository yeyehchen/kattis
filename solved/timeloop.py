import sys

lines = [line for line in sys.stdin]

N = int(lines[0])

for i in range(N):
    num = i + 1
    chant = str(num) + " Abracadabra"
    print(chant)
