import sys

lines = [line.strip() for line in sys.stdin]

line = lines[0].split()
Aset = [1, 1, 2, 2, 2, 8]
need =[]
for i in range(len(Aset)):
    num = Aset[i] - int(line[i])
    need.append(str(num))
x = ' '.join(need)
print(x)  