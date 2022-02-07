import sys

lines = [line.strip() for line in sys.stdin]

line = lines[0].split()

X = int(line[0])
Y = int(line[1])
N = int(line[2])

for i in range(N):
    i = i + 1
    if i % X == 0 and i % Y == 0:
        i = 'FizzBuzz' 
    elif i % X == 0:
        i = "Fizz"
    elif i % Y == 0:
        i = 'Buzz'  
    print(i)          
