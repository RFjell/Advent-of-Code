
current = 5

with open('input') as f:
    for line in f.readlines():
        for char in line:
            if char == 'U' and  current > 3:
                current -= 3
            elif char == 'D' and current < 7:
                current += 3
            elif char == 'L' and (current - 1) % 3 != 0 :
                current -= 1
            elif char == 'R' and current % 3 != 0:
                current += 1
        print(current, end = '')

