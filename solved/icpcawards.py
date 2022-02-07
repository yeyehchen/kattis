import sys

class Reader:

    def __init__(self):
        self.lines = [ line for line in sys.stdin]
        self.line_index = 0

    def get_ints(self):
        line = self.get_str()
        nums = [int(x) for x in line.split()]
        return nums

    def get_int(self):
        line = self.get_str()
        num = int(line)
        return num

    def get_str(self):
        line = self.lines[self.line_index] 
        self.line_index += 1
        return line


reader = Reader()
# Write solution below here


N = reader.get_int()
reward = {}
for _ in range(N):
    value = reader.get_str()
    school_team = value.split()
    if school_team[0]  in reward :
        continue
    if school_team[0]  not in reward :
        reward[school_team[0]] = school_team[1]
    if len(reward) >= 12:
        break    
    
for school in reward:
    print(school, reward[school]) 
    

    