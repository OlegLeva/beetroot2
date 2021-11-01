import time
from functools import wraps


def record_file(filenames):
    def reverce_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            value = func(*args, **kwargs)
            t2 = time.time()
            with open(filenames, 'a') as logies:
                logies.writelines(f'Execution time: {t2 - t1} result: {value} \n')
            return f'Execution time: {t2 - t1} result: {value}'

        return wrapper

    return reverce_time
def return_func_with_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func(*args, **kwargs)} !!!')
    return wrapper

@return_func_with_data
# @record_file('logfile.log')
def reverse(my_data):
    '''reverce all'''
    return (my_data[::-1])


print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(reverse('abcd'))
print(help(reverse))
