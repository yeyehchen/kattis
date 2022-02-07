import sys

lines = [ line.strip() for line in sys.stdin ]
n = int(lines[0])
speed_lis = []
for i in range(1,n):
    current_photo = lines[i].split()
    next_photo = lines[i+1].split()   
    t_diff = int(next_photo[0]) - int(current_photo[0])
    d_diff = int(next_photo[1]) - int(current_photo[1])
    speed = int(d_diff/t_diff)
    speed_lis.append(speed)
print(max(speed_lis))    
   
    
