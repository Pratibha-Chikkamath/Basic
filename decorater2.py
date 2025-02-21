def split(fun):
    def inner(a):
        b=fun(a)
        c=b.split(" ")
        return c
    return inner
@split
def str_fun(x):
    return x
b=str_fun("hello good morning palle")
print(b)
