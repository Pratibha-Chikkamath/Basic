#How do you call a parent class constructor which does not have parameters from the child class constructor show code
class A:
    def __init__(self):
        print("hiii palle")
class B(A):
    def __init__(self):
        super().__init__()
        print("Hello student")
b=B()

#how do you call parent class methods from child class?show code
#useing super() function
class A:
    def m1(self):
        print("hiii palle")
class B(A):
    def m2(self):
        super().m1()
        print("Hello student")
b=B()

#how do we access the parent class instance variable with child class object?show code
class A:
    def __init__(self):
        self.x=100
        print("hiii palle")
class B(A):
    def __init__(self):
        super().__init__()
        print("Hello student")
b=B()
print(b.x)

#How do we access the parent class self.x variable in child class method ? show code
class A:
    def __init__(self,x):
        self.x=x
        print("hiii palle")
class B(A):
    def __init__(self,x):
        super().__init__(x)
        print("Hello student x=",x)
b=B(10)




