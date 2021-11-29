from dataclasses import dataclass

# @dataclass
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # a: int
    # b: int

x = MyClass(4, 6)
y = MyClass(4, 6)
print(x)
print(x == y)

@dataclass(order=True)
class MyClass:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
    a: int
    b: int

x = MyClass(4, 6)
y = MyClass(4, 6)
z = MyClass(6, 4)
q = MyClass(3, 4)
print(x)
print(x == y)
print(x > q)
print(x < z)