import sys

lines = [line.strip() for line in sys.stdin]

N = int(lines[0])

if N % 2 == 0 :
    print('Bob')
else:
    print('Alice')     