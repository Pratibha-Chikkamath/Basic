def uppercase(func):
    def inner(a):
        b=func(a)
        return b.upper()
    return inner
@uppercase
def m1(x):
    return x
b=m1("apple")
print(b)