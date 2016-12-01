xaxis = 0
yaxis = 0
facing = 0 # N:0, E:90, S:180, W:270

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

    if facing == 0:
        yaxis += distance
    elif facing == 180:
        yaxis -= distance
    elif facing == 270:
        xaxis -= distance
    else:
        xaxis +=distance

print("Answer:", abs(xaxis) + abs(yaxis),"blocks")
