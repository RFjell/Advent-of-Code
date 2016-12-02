
x = 0
y = 2
grid = [[0,0,1,0,0],
        [0,2,3,4,0],
        [5,6,7,8,9],
        [0,'A','B','C',0],
        [0,0,'D',0,0]]

with open('input') as f:
    for line in f.readlines():
        for char in line:
            if char == 'U' and y>0 and grid[y-1][x] != 0:
                y -= 1
            elif char == 'D' and y<4 and grid[y+1][x] != 0:
                y += 1
            elif char == 'L' and x>0 and grid[y][x-1] != 0:
                x -= 1
            elif char == 'R' and x<4 and grid[y][x+1] != 0:
                x += 1
        print(grid[y][x], end = '')

