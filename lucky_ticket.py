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


# import pdb
#
#
# @decor_time
# def lucky_number_6():
#     counter = 0
#     for i1 in range(10):
#         print(f'i1 {i1}')
#         for i2 in range(10):
#             for i3 in range(10):
#                 for i4 in range(10):
#                     print(f'i4 {i4}')
#                     for i5 in range(10):
#                         for i6 in range(10):
#                             if i1 + i2 + i3 == i4 + i5 + i6: counter += 1
#                             # pdb.set_trace()
#     return counter
#
#
# print(lucky_number_6())


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


# @decor_time
# def lucky_ticket_():
#     count = 0
#     for n in range(1001, 1000000):
#         if sum([int(i) for i in (str(n)[:-3])]) == sum([int(i) for i in (str(n)[-3:])]):
#             count += 1
#     return count
#
#
# print(lucky_ticket_())
#
#
# @decor_time
# def lucky_ticket_(ticket_len):
#     count = 0
#     end_range = 10 ** ticket_len
#     start_range = 10 ** (ticket_len // 2) + 1
#     for n in range(start_range, end_range):
#         if sum([int(i) for i in str(n)[:-3]]) == sum([int(i) for i in (str(n)[-3:])]):
#             count += 1
#     return count
#
#
# print(lucky_ticket_())


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
#             if i < 3:
#                 sum_right += n // 10 ** i % 10
#             else:
#                 sum_left += n // 10 ** i % 10
#             if sum_left == sum_right:
#                 count += 1
#     return count


#
# print(lucky_ticket_())


# @decor_time
# def lucky_ticket_(x):
#     count = 0
#     for n in range(x):
#         n = str(n)
#         if len(n) > 1:
#             right = sum([int(i) for i in n[len(n) // 2:]])
#             left = sum([int(i) for i in n[:len(n) // 2]])
#             if right == left:
#                 count += 1
#
#     return count
#
#
# print(lucky_ticket_(1000000))


#
# x = 253352
#
# is_happy = lambda x: x % 1e3 % 9 == x // 1e3 % 9
# print(is_happy)

@decor_time
def lucky_ticket_all(ticket_len):
    count = 0
    end_range = 10 ** ticket_len
    start_range = 10 ** (ticket_len // 2) + 1
    for n in range(start_range, end_range):
        n = str(n)
        right = sum([int(i) for i in n[:-ticket_len // 2]])
        left = sum([int(i) for i in n[-ticket_len // 2:]])
        if right == left:
            count += 1

    return count


print(lucky_ticket_all(6))
