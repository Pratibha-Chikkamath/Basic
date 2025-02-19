#1)single inheritance
class Traing:
    def m1(self):
        print("i m trainer in clg")
class Student:
    def m2(self):
        print("i m study in bengalore")


t=Traing()
s=Student()
t.m1()
s.m2()

#multi-level inheritance
class Grandmother:
    def m1(self):
        print("teach to mom how to cook tasty food")
class Mother(Grandmother):
    def m2(self):
        print("prepare tasty food")
class Douther(Mother):
    def m3(self):
        print("eat tasty food")

d=Douther()
d.m3()
d.m2()
d.m1()