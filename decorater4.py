def sub(fun):
    def inner(a,b):
        c,d=fun(a,b)
        z=c-d
        return z
    return inner
@sub
def sub(x,y):
    return  (x,y)
z=sub(30,20)
print(z)