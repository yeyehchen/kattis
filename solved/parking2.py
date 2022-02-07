import sys

def dist(lis):

    def first(num, lis):
        return abs(num - lis[0])
    def end(num, lis):
        return abs(num - lis[-1])

    lis.sort()
           
    length = len(lis)
    if length%2 == 1:
        middle = lis[length//2]
        fist = first(middle,lis)
        last = end(middle,lis)
        return 2 * fist + 2 * last  
    else:
        middle_1 = lis[int(length/2)-1] 
        middle_2 = lis[int(length/2)]
        m1 = 2 * first(middle_1,lis) + 2 * end(middle_1,lis)
        m2 = 2 * first(middle_2,lis) + 2 * end(middle_2 ,lis)
        return min(m1, m2)    

lines = [ line.strip() for line in sys.stdin ]

'''
t = int(lines[0]) 
for i in range(1,t*2,2):
    n = int(lines[i])
    shop = [ int(num) for num in lines[i+1].split(" ") ]  
    #print(dist(shop))   


print(dist([24,13,89,37]))     
'''

def solve(stores):
    stores.sort()
    answer = float("inf")
    for store in stores:
        dist_left = abs(stores[0] - store)
        dist_right = abs(stores[-1] - store)
        total_dist = 2 * dist_left + 2 * dist_right
        answer = min(answer, total_dist)
    print(answer)

i = 1
while i < len(lines):
    n = int(lines[i])
    stores = [int(x) for x in lines[i+1].split()]
    ans = dist(stores)
    print(ans)
    #solve(stores)
    i += 2



