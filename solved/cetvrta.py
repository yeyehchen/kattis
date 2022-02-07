import sys

lines = [ line.strip() for line in sys.stdin ]
x = []
y = []
for i in range(3):
    p = [ int(x) for x in  lines[i].split()]
    x.append(p[0])
    y.append(p[1])
for num in x:
    if x.count(num) == 1 :
        a = num
for num in y:
    if y.count(num) == 1 :
        b = num
    

print(a,b)               
    
