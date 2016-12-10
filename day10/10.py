
class Bot:
    def __init__(self, number):
        self.number = number    #id
        self.instructions = []  #reference to bot or output
        self.items = []         #chips
    def add_instructions(self, instructions):
        self.instructions = instructions
    def add(self, item):
        if self.items == [] or self.items[0] < item:
            self.items.append(item)
        else:
            self.items.insert(0, item)
        if len(self.items) == 2:
            turn_list.append(self)
        if self.items == [17,61]:
            print("Answer to problem 1:",self.number)

class Output:
    def __init__(self):
        self.item = None
    def add(self,item):
        self.item = item

bots = [Bot(x) for x in range(210)]
outputs = [Output() for x in range(21)]
turn_list = []

#parse
with open('input') as f:
    lines = f.readlines()

for line in lines:
    a = line.split()
    if a[0] == 'value':
        bot, value = int(a[5]), int(a[1])
        bots[bot].add(value)
    else:
        bot, low, high = [int(x) for x in [a[1], a[6], a[11]]]
        r1, r2 = None, None

        r1 = bots[low] if a[5] == 'bot' else outputs[low]
        r2 = bots[high] if a[10] == 'bot' else outputs[high]

        bots[bot].add_instructions( [r1,r2] )

#execute
while len(turn_list) != 0:
    bot = turn_list.pop(0)
    r1, r2 = bot.instructions
    low, high = bot.items
    bot.items = []
    r1.add(low)
    r2.add(high)

#solve problem 2
res = 1
for o in outputs[:3]:
    res *= o.item
print("Answer to problem 2:",res)
