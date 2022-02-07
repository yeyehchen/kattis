import sys
import math

g = 9.81

def x(t, v0, degree):
    angle = degree * math.pi / 180
    return v0 * t * math.cos(angle)

def y(t, v0, degree):
    angle = degree * math.pi / 180
    return v0 * t * math.sin(angle) - 0.5 * g * t * t

def deg_to_rad(degree):
    return degree * math.pi / 180 

lines = [line.strip() for line in sys.stdin]

N = int(lines[0])

for i in range(N):
    case = lines[i+1].split()
    V = float(case[0])
    theta_deg = float(case[1])
    theta_rad = deg_to_rad(theta_deg)
    X = float(case[2])
    H1 = float(case[3])
    H2 = float(case[4])

    t = X/V/math.cos(theta_rad)
    Y = y(t, V, theta_deg)

    if H1 + 1 <= Y and Y <= H2 - 1:
        print ("Safe")
    else:
        print("Not Safe")    
    

    
