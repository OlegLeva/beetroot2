import random

i = 0
my_list = []
while i < 10:
    my_list.append(random.randint(0, 100))
    i += 1
print(my_list)
print(max(my_list))

i = 0
list_1 = []
list_2 = []
while i < 10:
    list_1.append(random.randint(0, 10))
    list_2.append(random.randint(0, 10))
    i += 1

print(list_1)
print(list_2)
list_3 = list(set(list_1) & set(list_2))
print(list_3)


i = 1
my_list_1 = []
list_result = []
while i < 101:
    my_list_1.append(i)
    i += 1

j = 0
while j < len(my_list_1):
    if my_list_1[j] % 7 == 0 and my_list_1[j] % 5 != 0:
        list_result.append(my_list_1[j])
    j += 1
print(list_result)

