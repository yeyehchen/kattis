import sys

lines = [line.strip() for line in  sys.stdin]
n = int(lines[0])

def is_harshad(number):
    total = 0
    lis_n = [int(x) for x in str(number)]
    for num in lis_n:
        total += num
    if number % total == 0:
        return True
    return False    

for i in range(n,1000000001,1):
    if is_harshad(i) == True:
        print(i)
        break 


 