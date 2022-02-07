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

data = reader.get_list(int)
D = data[0]
M = data[1]


# import Python's datetime module

import datetime

# weekdays as a tuple

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# Find out what day of the week is this year's Christmas

the_day = datetime.date(2009,M,D)

answer = the_day.weekday()

day = weekDays[answer]
print(day)
