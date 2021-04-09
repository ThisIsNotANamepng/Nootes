import cryptocode
from Cryptodome.Hash import SHA3_512
aa = ('create')


for i in range(10):

  if aa == ('create'):
    i = str(i)
    a = (i)
    b = (i)
    c = (i)
    obj = SHA3_512.new()
    obj.update(bytes((a), encoding='utf-8'))
    e = (obj.hexdigest())
    encoded = cryptocode.encrypt((b),(c))
    f = open((e) + ".txt", "w")
    f.write(encoded)
    f.close()
    print (encoded)


