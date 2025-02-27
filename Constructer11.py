#call class method in instance method useing Class name
class Example:
    def instance_method(self):
        print("This is an instance method")
        Example.class_method()

    @staticmethod
    def static_method():
         print("This is a static method")

    @classmethod
    def class_method(cls):
         print("This is a class method")

# Creating an instance of Example
obj = Example()

# Calling methods
print(obj.instance_method())  # (1)
print(obj.static_method())    # (2)
print(obj.class_method())     # (3)

print(Example.static_method())  # (4)
print(Example.class_method())   # (5)
print(Example.instance_method())  # (6) ❌ Potential Error
