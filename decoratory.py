import time
from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        value = func(*args, **kwargs)
        t2 = time.time()
        print(f'Execution time {t2 - t1}')
        return value
    return wrapper


@decor
def sqrt_1(x, y):
    '''SQRT'''
    return x ** y


print(sqrt_1(100, 1000))
print(help(sqrt_1))

def decor_time(file_name):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            value = func(*args, **kwargs)
            t2 = time.time()
            print(f'Execution time {t2 - t1}')
            with open(file_name, 'a') as loger:
                loger.writelines(f'Execution time {t2 - t1} {value} \n')
            return value
        return wrapper
    return decor


@decor_time('logfile.log')
def upper_1(word):
    return word.upper()

print(upper_1('uuuuuuuu'))
print(help(upper_1))
