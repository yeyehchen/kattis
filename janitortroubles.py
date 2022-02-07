import sys
import math

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
vertices = reader.get_list(int)
a = vertices[0]
b = vertices[1]
c = vertices[2]
d = vertices[3]

angle = degree * math.pi / 180
#area = 0.5 a × d × sin A + 0.5 × b × c × sin C