#How do you call a parent class constructor which has parameter x from the child class constructor show code
class A:
    def __init__(self,x):
        self.x=x
        print("parent class constructor called x=",x)
class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
        print("Child class constructor called y=",y)
b=B(10,20)

#3
class A:
    def __init__(self):
        print("hiii palle")
class B(A):
    def __init__(self):
        super().__init__()
        print("Hello student")
b=B()

