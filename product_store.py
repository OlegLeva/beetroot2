class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore(Product):
    def __init__(self, type, name, price, amount=0):
        super().__init__(type, name, price)
        self.amount = amount

    def add(self, price, amount):
        self.price *= 1.3
        self.amount += amount