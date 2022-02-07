import sys
import math

lines = [ line.strip() for line in sys.stdin ]
N = int(lines[0])

for i in range(1,N+1):
    poem = lines[i]
    amount = len(lines[i])
    side = int(math.sqrt(amount))
    newpoem = []
    for i in range(side) :
        line = poem[i*side:(i+1)*side]
        newpoem.append(line)
    finalpoem =[]
    for a in range(side):
        for word in newpoem:
            finalpoem += word[side-a-1]      
    print("".join(finalpoem))  



    