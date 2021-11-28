from random import randint

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
