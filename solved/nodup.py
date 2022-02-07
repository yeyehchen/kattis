import sys

lines = [line.strip() for line in sys.stdin]

line = lines[0].split()
pharse = {}
for word in line:
    if word not in pharse:
        pharse[word] = 1
    else :
        pharse[word] += 1    
for word in pharse:
    if pharse[word] > 1:
        break
        x = 'no'
    else:
        x = 'yes'          
print(x)
        
