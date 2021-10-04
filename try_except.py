def oops():
    raise IndexError("opa")

try:
    oops()
except (IndexError):
    print('ok')


def divided():
    x = int(input('Enter number 1: '))
    y = int(input('Enter number 2: '))
    return x*x/y
try:
    print(divided())
except ValueError:
    print('It is not number')
except ZeroDivisionError:
    print('cannot divide by zero')