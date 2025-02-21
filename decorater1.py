def squre(func):
    def inner(a):
        b=func(a)
        return [i ** 2 for i in func(a)]
    return inner
@squre
def m1(x):
    return x
print(m1([10,20,30,40,50]))
