import operator

with open('input') as f:
    lines = f.readlines()

res = ''

for i in range(len(lines[0])):
    line_info = {}
    for j in range(len(lines)):
        char = lines[j][i]
        if char in line_info:
            line_info[char] += 1
        else:
            line_info[char] = 1

    sorted_char_count = sorted(line_info.items(), key=operator.itemgetter(0))
    sorted_char_count = sorted(sorted_char_count, key=operator.itemgetter(1),
                               reverse=True)
    res += sorted_char_count[0][0]
print(res)
