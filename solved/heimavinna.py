import sys

lines = [ line.strip() for line in sys.stdin ]

x = lines[0].split(";")
total = 0
for i in range(len(x)):
    if "-" in x[i]:
        #get 2 number start and end 
        get_two = x[i].split("-")
        s = int(get_two[0])
        e = int(get_two[1])
        total += len(range(s,e+1))
    else :
        total += 1
print(total)            