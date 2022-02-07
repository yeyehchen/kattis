import sys

lines = [ line.strip() for line in sys.stdin ]
n = int(lines[0])
correct = 0
hans= []
for i in range(1,n):
    if lines[i] == lines[i+1]:
        correct += 1
    
print(correct)        