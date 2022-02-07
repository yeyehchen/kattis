import sys

lines = [line.strip() for line in sys.stdin]

N = lines[0].split("-")
short = ""

for name in N:
    short += name[0]
print(short)    