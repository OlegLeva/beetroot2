from random import randint


class Stack:
    def __init__(self):

        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) < 1:
            raise Exception('stack empty')
        return self.items.pop()

    def max(self):
        res = 0
        stack_2 = []
        while self.items:
            val = self.items.pop()
            if val > res:
                res = val
            stack_2.append(val)
        while stack_2:
            val = stack_2.pop()
            self.items.append(val)
        return res



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


def coin():
    return randint(0, 1)


def dice():
    res = 1
    for _ in range(5):
        res += coin()

    return res


print(dice())


# def test_dice(func):
#     dict_test = {}
#     for _ in range(100):
#         v = func
#         if dict_test[v] not in dict_test: dict_test[v] = 1
#         else: dict_test[v] += 1
#
#     return dict_test
#
# print(test_dice(dice()))

def test_dice(func):
    dict_test = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(1000):
        dict_test[func] += 1
    return dict_test


print(test_dice(dice()))
