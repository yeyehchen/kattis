import sys

lines = [line.strip() for line in sys.stdin]

L = lines[0]
D = lines[1]
X = lines[2]

numL = int(L)
numD = int(D)
numX = int(X)
A =[]

for i in range(numL, numD+1):
    HB = len(D)
    first = int(i/10**(HB-1))
    second = int((i-first*10**(HB-1))/10**(HB-2))
    third = int((i-first*10**(HB-1) - second*10**(HB-2)) /10**(HB-3))
    forth = int((i-first*10**(HB-1) - second*10**(HB-2) - third*10**(HB-3))/10**(HB-4))
    fifth= int(i-first*10**(HB-1)- second*10**(HB-2) - third*10**(HB-3) - forth*10**(HB-4))
    if first + second + third + forth + fifth == numX:
        A.append(i)
N = min(A)
M = max(A)
print(N)
print(M)

    
         

    

