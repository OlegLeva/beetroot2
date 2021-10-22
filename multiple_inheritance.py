class Person:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age

    def eat(self):
        return "He ate!"


class Vegitarian(Person):
    def __init__(self, name, age, vegitarian_eat, *args, **kwargs):
        super().__init__(name, age, *args, **kwargs)
        self.vegitarian_eat = vegitarian_eat

    def eat_salad(self):
        return "Dilishion salad"

    def poped(self):
        return f"{self.name} pooped softly"


class Meat_eater(Person):
    def __init__(self, name, age, meat_eat, *args, **kwargs):
        super().__init__(name, age, *args, **kwargs)
        self.meat_eat = meat_eat

    def eat_meat(self):
        return "Fat meat"

    def poped(self):
        return f"{self.name} pooped hard"


class NormalMan(Meat_eater, Vegitarian):
    def __init__(self, name, age, meat_eat, vegitarian_eat):
        super().__init__(name, age, meat_eat, vegitarian_eat)


norm_man = NormalMan('Max', 43, 'pork', 'eggplant')
print(norm_man.poped())
