
count = 0

with open('input') as f:
    lines = [a.split() for a in f.readlines()]

    x = range(len(lines))
    for i in x[0::3]:
        for k in range(3):
            (a,b,c) = (int(lines[i][k]),int(lines[i+1][k]),int(lines[i+2][k]))
            if a+b>c and a+c>b and b+c>a:
                count += 1

print(count)
