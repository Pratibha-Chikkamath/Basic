
class A:
     def m1(self):
         print("hiii")
class B(A):
    def m2(self):
        super().m1()
        print("helooo")
b=B()
b.m2()