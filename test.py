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

#
# class Dictionary():
#     def __init__(self):
#         self.my_dict = {}
#
#     def newentry(self, word, definition):
#         self.my_dict[word] = definition
#
#     def look(self, key):
#         if key not in self.my_dict:
#             return f"Can't find entry for {key}"
#         return self.my_dict[key]


#
# def ones_counter(inp):
#     counter = 0
#     res = []
#     for n in inp:
#         if n == 1:
#             counter += 1
#         else:
#             if counter != 0:
#                 res.append(counter)
#                 counter = 0
#     if counter != 0:
#         res.append(counter)
#
#     return res
#
# print(ones_counter([1,1,1,0,0,1,1,0,1]))

# def elevator_distance(array):
#     res = 0
#     index = 0
#     while index < len(array) - 1:
#         n = array[index] - array[index+1]
#         index += 1
#         if n < 0:
#             n = -n
#         res += n
#     return res
#
# print(elevator_distance([5,2,8]))

#
# def two_oldest_ages(ages):
#     x = ages.pop(ages.index(max(ages)))
#     y = ages.pop(ages.index(max(ages)))
#
#     return [y, x]
#
# print(two_oldest_ages([1, 3, 10, 0]))

# def number_of_pairs(gloves):
#     new_list = []
#     res = 0
#     for color in gloves:
#         if color not in new_list and gloves.count(color) > 1:
#             new_list.append(color)
#             res += gloves.count(color)
#
#     return res//2
#
# print(number_of_pairs(["red","green","blue"]))
#
# def faro_cycles(deck_size):
#     deck = list(range(deck_size))
#
#     middle = len(deck) // 2
#     count = 1
#     new_deck = []
#     left = deck[:middle]
#     right = deck[middle:]
#     while left or right:
#         new_deck.append(left.pop(0))
#         new_deck.append(right.pop(0))
#     print(new_deck)
#     while deck != new_deck:
#         left1 = new_deck[:middle]
#         right1 = new_deck[middle:]
#         new_deck = []
#         while left1 or right1:
#             new_deck.append(left1.pop(0))
#             new_deck.append(right1.pop(0))
#         count += 1
#
#
#
#     return count
#
# print(faro_cycles(52))
#
# deck_size = 52
# arr= list(range(deck_size))
# arr = arr[0:deck_size:2] + arr[1:deck_size:2]
# arr = arr[0:deck_size:2] + arr[1:deck_size:2]
# print(arr)
#
# def get_participants(handshakes):
#     hand = 0
#     hand_list = []
#     while sum(hand_list) != handshakes:
#         hand += 1
#         hand_list.append(hand)
#     return hand_list[-1] + 1
#
#
# print(get_participants(10))

#
#
# def sort_bublle(lst):
#     i = len(lst)-1
#     while i:
#     # for i in range(len(lst)-1,0,-1):
#         for j in range(i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#         i -= 1
#
#     return lst
#
# print(sort_bublle([19,2,31,45,6,11,121,27]))
#
# def insertion_sort(InputList):
#    for i in range(1, len(InputList)):
#       j = i-1
#       nxt_element = InputList[i]
#       print(f'{i} i')
#       print(nxt_element)
#       while (InputList[j] > nxt_element) and (j >= 0):
#             InputList[j+1] = InputList[j]
#             j=j-1
#             InputList[j+1] = nxt_element
# list = [19,2,31,45,30,11,121,27]
# insertion_sort(list)
# print(list)

def insert_sort(lst):
    for i in range(1, len(lst)):
        next_item = lst[i]
        j = i - 1
        print(j)
        while j >= 0 and lst[j] > next_item:
            print(f'j = {j}')
            lst[j+1] = lst[j]
            j -= 1
            lst[j + 1] = next_item

    return lst


print(insert_sort([19,2,31,45,30,11,121,27]))




