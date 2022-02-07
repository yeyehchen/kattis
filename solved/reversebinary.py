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

N = reader.get(int)
print(int(str(bin(N))[2:][::-1], 2))

#explain
binary_N = bin(N)
print(binary_N)
binary_N_string = str(binary_N)[2:]
print(binary_N_string)
binary_N_reverse = binary_N_string[::-1]
print(binary_N_reverse)
answer = int(binary_N_reverse, 2)
print(answer)


