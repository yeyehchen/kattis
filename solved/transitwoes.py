import sys
lines = [line.strip() for line in sys.stdin]

line = lines[0].split()

s = int(line[0])
t = int(line[1])
n = int(line[2])

d = [int(x) for x in lines[1].split()]
b = [int(x) for x in lines[2].split()]
c = [int(x) for x in lines[3].split()]

time = 0

for i in range(n):
    # Walk to bus i
    time += d[i]
    # Wait for bus i
    last_time_bus = (time // c[i]) * c[i]
    if last_time_bus != time:
        wait_bus = last_time_bus + c[i] - time
        time += wait_bus
    # Ride bus i
    time += b[i]
time += d[-1]
"""
    bus = int(c[i])
    walk += int(d[i])
    ride += int(b[i])
    waitbus += (bus - walk)   
    times = walk + waitbus + ride
total = times + int(d[-1])
"""


if t >= time:
    print('yes')
else:
    print('no') 

"""
wait ={}
bus = int(c[i])
walk += int(d[i])
ride += int(b[i])
if c[0] > d[0]:
    wait[0] = c[0] - d[0]
    wait[1] = (wait[0] + b[0] + d[1])% c[1]
"""



