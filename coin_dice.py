from random import randint


def coin():
    return randint(0, 1)


def dice():
    res = 1
    for _ in range(5):
        res += coin()
    return res



# def test_dice():
#     dict_test = {}
#     for _ in range(1000):
#         v = dice()
#         print(v)
#         if dict_test[v] not in dict_test:
#             dict_test[v] = 1
#         else:
#             dict_test[v] += 1
#
#     print(dict_test)
#
# test_dice()

def test_dice():
    dict_test = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(1000000):
        dict_test[dice()] += 1
    print(dict_test)


test_dice()
