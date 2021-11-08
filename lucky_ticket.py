import time
from functools import wraps


def decor_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        value = func(*args, **kwargs)
        t2 = time.time()
        print(f'Execution time {t2 - t1}')
        return value
    return wrapper

# @decor_time
# def lucky_ticket_():
#     count = 0
#     in_the_range = list(range(1000, 1000000))
#     for n in in_the_range:
#         lst = []
#         while n:
#             lst.append(n % 10)
#             n //= 10
#         if sum(lst[:-3]) == sum(lst[-3:]):
#             count += 1
#
#
#     return count
#
#
# print(lucky_ticket_())



@decor_time
def lucky_ticket_():
    count = 0
    in_the_range = range(1000, 1000000)
    for n in in_the_range:
        if sum([int(i) for i in (str(n)[:-3])]) == sum([int(i) for i in (str(n)[-3:])]):
            count += 1
    return count

print(lucky_ticket_())

# @decor_time
# def lucky_ticket_(x):
#     count = 0
#     in_the_range = list(range(1000, x))
#     for n in in_the_range:
#         if sum([int(i) for i in (str(n)[:-(len(str(n))//2)])]) == sum([int(i) for i in (str(n)[-(len(str(n))//2):])]):
#             count += 1
#     return count
#
# print(lucky_ticket_(1000000))
#
# @decor_time
# def lucky_ticket_():
#     count = 0
#     sum_left = 0
#     sum_right = 0
#     in_the_range = list(range(1000, 1000000))
#     for n in in_the_range:
#         for i in range(len(str(n))):
#             if i<3:
#                 sum_right += n // 10**i % 10
#             else:
#                 sum_left  += n // 10**i % 10
#             if sum_left == sum_right:
#                 count += 1
#     return count
#
# print(lucky_ticket_())


@decor_time
def lucky_ticket_(x):
    count = 0
    for n in range(x):
        n = str(n)
        if len(n) > 1 and len(n) % 2 == 0:
            right = sum([int(i) for i in n[len(n)//2:]])
            left = sum([int(i) for i in n[:len(n)//2]])
            if right == left:
                count += 1

        if len(n) > 1 and len(n) % 2 != 0:
            right = sum([int(i) for i in n[len(n)//2+1:]])
            left = sum([int(i) for i in n[:len(n)//2]])
            if right == left:
                count += 1

    return count

print(lucky_ticket_(1000000))

x = 253352

is_happy = lambda x: x % 1e3 % 9 == x // 1e3 % 9
print(is_happy)



