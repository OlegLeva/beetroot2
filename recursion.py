# new_list = []
# def list_reverse(n: list):
#     if len(n) == 0:
#         return
#     new_list.append(n.pop())
#     list_reverse(n)
#
#
# list_reverse([1,2,3,4,5])
#
# print(new_list)

def list_reverse(n: list):
    if len(n) == 0:
        return
    print(n.pop())
    list_reverse(n)


list_reverse([1, 2, 3, 4, 5])


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


print(f'"!5" {factorial(6)}')


def fibonachi(n):
    """[1, 1, 2, 3, 5, 8]"""
    x = 1
    y = 0
    my_list = []
    while len(my_list) != n:
        my_list.append(x)
        x = x + y
        y = x - y
    return my_list


print(fibonachi(6))


def fibonacci(n):
    if n in (1, 2):
        return 1
    # print(fibonachi(n))
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
