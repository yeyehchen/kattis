import sys

lines = [line for line in sys.stdin]

line = lines[0]

def hissOrNo():
    for i in range(len(line) - 1):
        if line[i] == line[i + 1] and line[i] == 's':
            return True
        
if hissOrNo():
     print("hiss")
else :
     print("no hiss")       
       
 
        
