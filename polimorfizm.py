class Animals:
    def talk(self):
        return "Kuku"

class Dog:
    def talk(self):
        return "woof woof"

class Cat:
    def talk(self):
        return "meow"

def universal(animal):
    print(animal.talk())

sharik = Dog()
murzik = Cat()

universal(murzik)
universal(sharik)
