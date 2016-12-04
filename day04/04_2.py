import operator

with open('input') as f:
    lines = [ x.strip() for x in f.readlines()]
for line in lines:
    linesplit = line.split('-')
    name = linesplit[:-1]
    (idnbr,checksum) = linesplit[-1].split('[')
    checksum = checksum[:-1]

    char_count = {}
    for word in name:
        for char in word:
            if not char in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

    sorted_char_count = sorted(char_count.items(), key=operator.itemgetter(0))
    sorted_char_count = sorted(sorted_char_count, key=operator.itemgetter(1),
                              reverse = True)
    if(''.join( [ x[0] for x in sorted_char_count[:5]]) == checksum):
        shift = int(idnbr) % 26
        real_name = ''
        for word in name:
            for char in word:
                new_char = ord(char) + shift
                if new_char > ord('z'):
                    new_char -= 26
                real_name += chr(new_char)
            real_name += ' '
        if 'northpole' in real_name:
            print(idnbr,real_name)

