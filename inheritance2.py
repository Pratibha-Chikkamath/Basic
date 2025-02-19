#3)multiple inheritance
class Grandmother:
    def m1(self):
        print("teach to mom how to cook tasty food")
class Mother:
    def m2(self):
        print("prepare tasty food")
class Douther(Grandmother,Mother):
    def m3(self):
        print("eat tasty food")

d=Douther()
d.m1()
d.m2()
d.m3()