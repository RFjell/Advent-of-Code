xaxis = 0
yaxis = 0
facing = 0 # N:0, E:90, S:180, W:270
grid = {}
grid[(xaxis,yaxis)] = 1

def travel(distance):
    global xaxis, yaxis
    (x, y) = (0,0)
    if facing == 0:
        y = 1
    elif facing == 180:
        y = -1
    elif facing == 270:
        x = -1
    else:
        x = 1
    for i in range(distance):
        xaxis += x
        yaxis += y
        if (xaxis,yaxis) in grid:
            return True
        grid[(xaxis,yaxis)] = 1

file = open('input')
content = file.read()
file.close()

for instruction in content.split(', '):
    direction = instruction[:1]
    distance = int(instruction[1:])

    if direction == 'R':
        facing = (facing + 90) % 360
    else:
        facing = (facing - 90) % 360
    if travel(distance):
        break

print("Answer:", abs(xaxis) + abs(yaxis),"blocks")
