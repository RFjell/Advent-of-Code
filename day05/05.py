
import hashlib

room_id = 'ugkcyxxp'
index = 0
res = ''
while len(res) < 8:
    m = hashlib.md5()
    m.update((room_id+str(index)).encode('ascii'))
    hexhash = m.hexdigest()
    if hexhash[:5] == '00000':
        res += hexhash[5]
        print(res)
    index += 1
print(res)
