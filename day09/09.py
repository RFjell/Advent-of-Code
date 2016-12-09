
with open('input') as f:
    line = f.readline()

res = ''
i = 0

while i < len(line):
    c = line[i]
    if c == '(':
        expr_end = line.find(')', i)
        expr = line[ i+1 : expr_end ]
        chars, count = [ int(x) for x in expr.split('x') ]
        i = expr_end + 1

        r = line[ i : i+chars ]
        res += r * count
        i += chars
    else:
        res += c
        i += 1

print( len(''.join( filter(lambda x: not x.isspace(), res) )))
