from dataclasses import dataclass

# @dataclass()
class Children:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



nik = Children('Nikita', 16)
john = Children('John', 7)

print(nik.age)
nik.age = 17
print(nik.age)
print(john.name, john.age)
