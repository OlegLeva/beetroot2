import random

def make_operation(operation, *args):

    if operation == "*":
        total = 1
        for i in args:
            total *= i
        return total
    if operation == "+":
        return sum(args)
    if operation == "-":
        total = args[0] - sum(args[1:])
        return total




print(make_operation("*", 4, 5, 3, ))
print(make_operation("-", 4, 5, 3, ))
print(make_operation("+", 4, 5, 3, ))

print([i for i in range(7)])

def print_tree(n):
    for i in range(n):
        for j in range(n-i):
            print(" ", end='')
        for k in range(i*2 + 1):
            print("*", end='')
        print()

print_tree(7)





ws = input('Введите слово: ')
w = list(ws)
i = 0
w_s = []
while i < 5:
    random.shuffle(w)
    word_shuffle = ''.join(w)
    w_s.append(word_shuffle)
    i += 1

print((w_s))
