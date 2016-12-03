
count = 0

with open('input') as f:
    for line in f.readlines():
        (a,b,c) = map(int, line.split())
        if a+b>c and a+c>b and b+c>a:
            count += 1

print(count)
