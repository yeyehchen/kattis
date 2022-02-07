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

dic = {"A":0 ,"B":1,"C":2,"D":3,"E":4,
       "F":5,"G":6,"H":7,"I":8,"J":9,
       "K":10,"L":11,"M":12,"N":13,"O":14,
       "P":15,"Q":16,"R":17,"S":18,"T":19,
       "U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}

rotate = len(dic)
data = reader.get(str)
length = len(data)
len_element = int(length/2)
twoword = [data[:len_element],data[len_element:-1]]
step2 = []
for word in twoword:
    total = 0
    for ch in word:
        total += dic[ch]
    movement = total%26  
    newword = []  
    for ch in word:
        new_index = (dic[ch]+ movement)%26
        for k, v in dic.items():
            if v == new_index:
                newword.append(k)
    change1 = "".join(newword)
    step2.append(change1) 
step3 = []
for i in range(len_element):
    a = step2[0][i]
    b = step2[1][i]
    x = (dic[a] + dic[b])%26
    finalword = []
    for k, v in dic.items():
        if v == x:
            finalword.append(k)
    change2 = "".join(finalword)            
    step3.append(change2)
end = "".join(step3)   
print(end)    
    



 
