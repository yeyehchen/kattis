import sys

lines = [line.strip() for line in sys.stdin]

num = lines[0].split()
num1 = num[0]
num2 = num[1]


def reverse(num):
    Nnum = []
    for i in range(len(num)):
        index = int(len(num)-(i+1))
        Nnum.append(num[index])
    n = "".join(Nnum)    
    return int(n)    

x = max(reverse(num1),reverse(num2))
print(x)




