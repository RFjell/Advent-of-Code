
with open('input') as f:
    l = f.readlines()

def explode(line):
    res, i = 0, 0
    while i < len(line):
        if line[i] == '(':
            expr_end = line.find(')', i)
            expr = line[ i+1 : expr_end ]
            chars, count = [ int(x) for x in expr.split('x') ]
            ending = expr_end + chars + 1
            tmp = chars

            if '(' in line[ expr_end + 1 : ending ]:
                tmp = explode( line[ expr_end + 1 : ending ])
            i = ending
            res += tmp * count
        else:
            res += 1
            i += 1
    return res

[print( explode(i.rstrip())) for i in l]
