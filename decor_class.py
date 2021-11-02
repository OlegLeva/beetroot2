from functools import wraps

class TypeDecorators:

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        return wrapper

    def to_int(self, value):
        if value.isdigt():
            return int(value)
        else:
            raise TypeError('wrong type')



    # to_str
    #
    # to_bool
    #
    # to_float
@TypeDecorators.to_int
def print_dig_str(str_dig):
    return str_dig

print(print_dig_str('55'))