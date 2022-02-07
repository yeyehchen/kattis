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
        return int(line)

    def get_str(self):
        line = self.lines[self.line_index] 
        self.line_index += 1
        return line

    def get_float(self):
        line = self.get_str()
        return float(line)

    def get(self, type_of_data):
        line = self.get_str()
        return type_of_data(line)

    def get_list(self, type_of_data):
        line = self.get_str()
        nums = [type_of_data(x) for x in line.split()]
        return nums

reader = Reader()
# Write solution below here

data = reader.get_list(str)
Y = data[0]
P = data[1]
vowel = ["a", "i", "o", "u" ]
if Y[-1] == "e":
    a = Y + "x" + P
elif Y[-1] in vowel:
    a = Y[:-1] + "ex" + P  
elif Y[-2:] == "ex":
    a = Y + P 
else:
    a = Y + "ex" + P    
print(a)    