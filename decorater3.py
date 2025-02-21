def add(fun):
    def inner(a,b):
        c,d=fun(a,b)
        z=c+d
        return z
    return inner
@add
def add(x,y):
    return  (x,y)
z=add(10,20)
print(z)