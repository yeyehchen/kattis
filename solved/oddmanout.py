import sys

lines = [line.strip() for line in sys.stdin]
N = int(lines[0])
i = 0
for C in lines[2::2]:
    case = C.split()
    id_count = {}
    for num in case:
        if num not in id_count:
            id_count[num] = 1
        else:
            id_count[num] += 1           
    for key, value in id_count.items():        
        if  value == 1:
            i += 1 
            print(f"Case #{i}: {key}")              
