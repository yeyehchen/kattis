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
        return line.strip()


reader = Reader()
# Write solution below here
num_lines = reader.get_int()
for _ in range(num_lines):
    value = reader.get_str()
    print(len(value))