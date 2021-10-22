class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    amount = 0
    profit = 0
    warehouse = []

    def add(self, product, amount):
        d = {}
        d['product'] = product
        d['amount'] = amount
        product.price *= 1.3
        self.warehouse.append(d)
    print(warehouse)


apple = Product('fruit', 'apple', 1.8)
apple_store = ProductStore()
apple_store.add(apple, 10)
print(apple.price)
print(apple_store.warehouse[0]['product'])
print(Product.mro())



