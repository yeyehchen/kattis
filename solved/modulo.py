import sys

lines = [line for line in sys.stdin]


def numOfModulo():
    difs = [] 
    for num in lines:
        num = int(num)
        dif = num % 42
        if dif not in difs:
            difs.append(dif)
    print(len(difs))      

numOfModulo()