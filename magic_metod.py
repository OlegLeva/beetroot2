class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

oleg = Person('Oleg', 42)
alex = Person('Alex', 42)
print(id(oleg))
print(id(alex))

if oleg == alex:
    print("They have the same age")


# txt = "They have the same age".split()
# index = 0
# while True:
#     print(txt[index])
#     index = (index + 1) % len(txt)
#     print(index)
