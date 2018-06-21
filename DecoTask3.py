import functools

def once(foo):
    @functools.wraps(foo)
    def inner(arg, n='Hi!'):
        n1=n        
        n=arg*2
        return foo(n1, n)
    return inner

def init(arg, n='Hello!'):
    print(n)
    return(arg)

print(init(9))
print(once(init)(9))