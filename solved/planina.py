import sys
import math

lines = [line for line in sys.stdin]

def ans(N):
    if N == 0:
        return 4
    return (2 * math.sqrt(ans(N - 1)) - 1) ** 2


x = int(lines[0])

print(int(ans(x)))
