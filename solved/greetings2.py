import sys

lines = [line.strip() for line in sys.stdin]

message = lines[0]

count = 0
for ch in message:
    if ch == "e":
        count += 1
newM = "h" + "e"*(count*2) + "y" 
print(newM)