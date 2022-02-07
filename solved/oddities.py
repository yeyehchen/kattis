import sys


lines = [line.strip() for line in sys.stdin]

N = int(lines[0])

for i in range(N):
    num = int(lines[i+1])
    if num%2 == 0:
        print(str(num) + " is even") 
    else:
        print(str(num) + " is odd")    