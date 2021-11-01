from functools import wraps


def change_text(my_list):
    def return_text(func):
        def wrapper(*args):
            text = func(*args)
            print(text)
            for w in my_list:
                text = text.replace(w, '*')
            return text

        return wrapper

    return return_text


@change_text(['pepsi', 'BMW'])
def drink(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(drink('Oleg'))


def arg_rules(type_, max_length, contains):
    def intermedia(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            name, = args
            if any(ext in name for ext in contains) and type(name) == type_ and len(name) <= max_length:
                return value
            else:
                return False

        return wrapper

    return intermedia


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))


