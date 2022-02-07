import sys

dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0 
} 

not_dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0 
} 

lines = [line.strip() for line in sys.stdin]

line = lines[0].split()
N = int(line[0])
B = line[1]

gamecard = []

for i in range(N*4):
    gamecard.append(lines[i+1])
D = []
ND = []
for round in gamecard :
    if round[1] == B:
        D.append(round[0])
    else:
        ND.append(round[0])    
        
total = 0

for card in D:
    total += dominant[card]

for card in ND:
    total += not_dominant[card]
print(total)    
     