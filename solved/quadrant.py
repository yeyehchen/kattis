import sys

lines = [line.strip() for line in  sys.stdin]
a = int(lines[0])
b = int(lines[1])

def which_quadrant(x,y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x > 0 and y < 0:
        return 4
    else:
        return 3           

print(which_quadrant(a,b))