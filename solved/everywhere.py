import sys

# lines = [line.strip() for line in sys.stdin]

# T = int(lines[0])
# n = int(lines[1])
# length = len(lines)
# trip = []
# startIndex = 0
# endIndex  = 0
# count = []
# for i in range(T):
#     trips = []
#     startIndex = 2 + i
#     endIndex = 2+ n + i
#     print(startIndex)
#     print(endIndex)
#     trips.append(lines[startIndex : endIndex])
#     startIndex = endIndex + i
#     endIndex = length - i
#     print(startIndex)
#     print(endIndex)
#     print(trips)
#for i in range(T):
    #times = {}
    #for trip in range(n):
        #if trip in times :
            #times[trip] += 1
        #else:
            #times[trip] = 1
    #count.append(times)
#print(count)  

def solve_cities(cities):
    # Remove the print and code to solve one test case
    print(cities)

lines = [line.strip() for line in  sys.stdin]
T = int(lines[0])
line_index = 1

for _ in range(T):
    n = int(lines[line_index])
    line_index += 1
    cities = []
    for _ in range(n):
        cities.append(lines[line_index])
        line_index += 1
    times = {}    
    for city in cities:
        if city in times:
            times[city] += 1
        else:
            times[city] = 1
    print(len(times))            
    