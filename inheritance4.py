#4)diamon or hybride inheritance
class A:
    def m1(self):
        print("i m a class")
class B(A):
    def m2(self):
        print("i m b class")
class C(A):
    def m3(self):
        print("i m c class ")
class D(B,C):
    def m4(self):
        print("i m d class")
d=D()
d.m1()
d.m2()
d.m3()
d.m4()
