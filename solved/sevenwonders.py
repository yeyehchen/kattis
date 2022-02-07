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
cards = reader.get(str)
cards = cards.strip()

count_card= {}
for card in cards:
    if card not in count_card:
        count_card[card] = 1
    else:
        count_card[card] += 1        
total = 0
for card in count_card:
    total += count_card[card] **2
if "T" in count_card and "C" in count_card and "G" in count_card:
    key_min = min(count_card.keys(), key=(lambda card: count_card[card]))
    set_card = count_card[key_min]
    total += set_card *7
       
print(total)    

    
  