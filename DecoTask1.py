import hashlib
import functools

@functools.singledispatch
def hash(arg):
    type_name = type(arg).__name__
    assert False, "Неподдерживаемый тип: " + type_name

@hash.register(str)
def _(arg):
    res = hashlib.md5(bytes(arg,'utf-8')).hexdigest()
    return res

@hash.register(list)
def _(arg):
    res = type(arg)()
    for i in arg:
        res.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return res

@hash.register(tuple)
def _(arg):
    res = []
    for i in arg:
        res.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return tuple(res)

@hash.register(set)
def _(arg):
    res = []
    for i in arg:
        res.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    return set(res)

@hash.register(dict)
def _(arg):
    keys = arg.keys()
    values = []
    for i in arg.values():
        values.append(hashlib.md5(bytes(i,'utf-8')).hexdigest())
    res = dict.fromkeys(keys,None)
    res.update(zip(keys,values))
    return res

print(hash('Doh!'))
print(hash({'Just':'Just', 'do':'do', 'it':'it'}))
