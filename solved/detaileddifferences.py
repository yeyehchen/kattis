import sys

lines = [ line.strip() for line in sys.stdin ]

N = int(lines[0])

for i in range(1,N+1):
    group = [lines[2*i-1] ,lines[i*2]]
    newcode = []     
    for i in range(len(group[0])):
        if group[0][i] == group[1][i]:
            newcode += "."
        else:
            newcode += "*" 
    newcode = "".join(newcode)        
    group.append(newcode)  
    for code in group :
        print(code) 
    print("")        


        
