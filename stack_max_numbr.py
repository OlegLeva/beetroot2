from random import randint


class Stack:
    def __init__(self):

        self.items = []
        self.max_value = 0

    def push(self, item):
        if item > self.max_value:
            self.max_value = item
        self.items.append(item)

    def pop(self):
        if len(self.items) < 1:
            raise Exception('stack empty')
        return self.items.pop()

    def max(self):
        res = 0
        for i in self.items:
            if i > res:
                res = i
        return res

    def max_val(self):
        return self.max_value


lst = Stack()
lst.push(44)
lst.push(66)
lst.push(333)
lst.push(32)

print(lst.max_val())
print(lst.max())
print(lst.items)
lst.pop()
print(lst.items)


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
#         if dict_test[v] in dict_test: dict_test[v] += 1
#         else: dict_test[v] = 1
#         print(dict_test)
#     return dict_test
#
# print(test_dice(dice()))

# def test_dice(func):
#     dict_test = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#     for _ in range(1000):
#         dict_test[func] += 1
#     return dict_test
#
# print(test_dice(dice()))

dict_test = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

print(2 in dict_test)


