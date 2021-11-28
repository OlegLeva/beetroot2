
class Stack:
    def __init__(self):

        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if not self.max_items:
            self.max_items.append(item)
        if self.max_items[-1] <= item:
            self.max_items.append(item)

    def pop(self):
        if len(self.items) < 1:
            raise Exception('stack empty')
        item_pop = self.items.pop()
        if item_pop == self.max_items[-1]:
            self.max_items.pop()
        return item_pop

    def max(self):
        return self.max_items[-1]



lst = Stack()
lst.push(44)
lst.push(66)
print(lst.items)
print(f'Max value {lst.max()}')
lst.push(333)
lst.push(32)
lst.push(444)

print(lst.items)
print(f'Max value {lst.max()}')
lst.pop()
lst.pop()
lst.pop()
print(lst.items)
print(f'Max value {lst.max()}')


