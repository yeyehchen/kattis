import sys

lines = [line.strip() for line in sys.stdin]

T = int(lines[0])
tests= []
for i in range(T):
    tests.append(lines[i+1])
for test in tests:
    test = test.split()
    f = 0
    p = 1
    for num in test:
        n = int(num)
        if p == n:
            f += 0
            p = n 
        elif p < n:
            plus  = n - p*2 
            if plus > 0:   
                f += plus
            else:
                f += 0    
            p = n

    print(f)




