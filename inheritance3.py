#4)hierarchical inheritance
class A:
    def m1(self):
        print("helooo")
class B(A):
    def m2(self):
        print("Hiiii")
class C(A):
    def m3(self):
        print("Good Morning")
c=C()
b=B()
c.m1()
b.m2()
c.m3()

