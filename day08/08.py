
height = 6
width = 50
grid = [[0 for x in range(width)] for y in range(height)]

def rect(A,B):
    for x in range(A):
        for y in range(B):
            grid[y][x] = 1

def rotate_row(row, count):
    for i in range(count):
        if grid[row][-1] == 1:
            grid[row] = [1] + grid[row][:-1]
        else:
            grid[row] = [0] + grid[row][:-1]

def rotate_column(col, count):
    for i in range(count):
        last = grid[-1][col]
        for j in range(height - 1,-1,-1):
            grid[j][col] = grid[j-1][col]
        grid[0][col] = 1 if last == 1 else 0

with open('input') as f:
    lines = f.readlines()

for line in lines:
    l = line.split()
    if l[0] == 'rect':
        rect(*[int(x) for x in l[1].split('x')])
    elif l[0] == 'rotate':
        index = int(l[2].split('=')[1])
        count = int(l[-1])
        if l[1] == 'row':
            rotate_row(index, count)
        elif l[1] == 'column':
            rotate_column(index, count)

res = 0
for y in grid:
    for i in range(len(y)):
        x = y[i]
        if i % 5 == 0:
            print(' ', end='')
        if x == 1:
            res += 1
            print('#', end='')
        else:
            print(' ', end='')
    print()
print()
print(res)

