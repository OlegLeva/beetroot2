from random import randint


def coin():
    return randint(0, 1)


def dice():
    while True:
        binary = str(coin())+str(coin())+str(coin())
        decimal = int(binary, 2)
        if decimal < 6: break
    return decimal

def dice_1():
    while True:
        binary = str(coin())+str(coin())+str(coin())
        decimal = int(binary, 2)
        if decimal < 6: break
    return decimal


def test_dice():
    dict_test = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for _ in range(1000000):
        dict_test[dice()] += 1
    print(dict_test)

print(test_dice())
print(dice())
print(dice())
print(dice())
print(dice())



x = "125"
y = '1928'
z = "2"