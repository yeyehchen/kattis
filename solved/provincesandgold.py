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

cards = reader.get_ints()
G = cards[0]
S = cards[1]
C = cards[2]

buying_power = G*3 + S*2 + C*1

if buying_power >= 8:
    print("Province or Gold")
elif 6 <= buying_power < 8 :
    print("Duchy or Gold")
elif 5 <= buying_power < 6:
    print("Duchy or Silver")
elif 3 <= buying_power < 5:
    print("Estate or Silver")
elif buying_power == 2:
    print("Estate or Copper")
else:
    print("Copper")    






