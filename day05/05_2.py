
import hashlib

room_id = 'ugkcyxxp'
index = 0
res = ['']*8
while len(''.join(res)) < 8:
    m = hashlib.md5()
    m.update((room_id+str(index)).encode('ascii'))
    hexhash = m.hexdigest()
    if hexhash[:5] == '00000' and hexhash[5] in '01234567' and \
                            res[int(hexhash[5])]== '':
        res[int(hexhash[5])] = hexhash[6]
        print(res)
    index += 1
print(''.join(res))
