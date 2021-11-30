# def fib():
#     numb, next_numb = 1, 1
#     while True:
#         yield numb
#         numb, next_numb = next_numb, numb + next_numb
#
#
# for i in (fib()):
#     if i % 12 == 0:
#         print("Всё приехали")
#         break
#     print(i)
#
#

# is_happy = lambda x: x % 1e3 % 9 == x // 1e3 % 9
# print(is_happy(253352))

# d = 8
# n = 10 ** d
# r = 10 ** (d // 2) + 1
#
# print(n, r)
#
# w = '12345'
# print(w[:-len(w) // 2])
# print(w[(-len(w) // 2):])
#
#
# def lucky_ticket_all(ticket_len):
#     count = 0
#     end_range = 10 ** ticket_len
#     start_range = 10 ** (ticket_len // 2) + 1
#     for n in range(start_range, end_range):
#         n = str(n)
#         right = sum([int(i) for i in n[:-ticket_len // 2]])
#         left = sum([int(i) for i in n[-ticket_len // 2:]])
#         if right == left:
#             count += 1
#
#     return count
#
#
# print(lucky_ticket_all(6))


integers_list = [-18, -31, 81, -19, 111, -888]
w = ''.join(str(e) for e in integers_list)
print(w)