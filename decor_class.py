from functools import wraps


class TypeDecorators:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        res = self.func(*args, **kwargs)
        return res

    def to_int(self, value):
        if value.isdigit():
            return int(value)
        else:
            raise TypeError('wrong type')

    


@TypeDecorators
def print_dig_str(str_dig):
    return str_dig


print(print_dig_str.to_int('22'))
print(type(print_dig_str.to_int('22')))
