def enum(lst):
    x = 0
    for y in lst:
        yield x, y
        x += 1


for e, i in enum(['a', 'b', 'c']):
    print(e, i)


def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


print(list(in_range(3, 21, 1)))


class MyList:
    def __init__(self, *args):
        self.args = args
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.args):
            raise StopIteration
        value = self.args[self.index]
        self.index += 1
        return value


my_lst = MyList(1, 2, 3, 4, )

# for i in my_lst:
#     print(i)

print(list(my_lst)[2])
