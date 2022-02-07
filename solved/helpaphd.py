import sys

lines = [ line.strip() for line in sys.stdin ]

N = int(lines[0])

for i in range(1,N+1):
    test = lines[i]
    
    if "+" in test:
        nums = test.split("+")
        total = 0
        for num in nums:
            num = int(num)
            total += num   
        print(total)
    if test == "P=NP" :
        print("skipped")