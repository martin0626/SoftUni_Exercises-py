def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return


def multiply(x, y):
    return x * y


def math_operations(*args, **kwargs):
    mapper = {'a': add, 's': subtract, 'd': divide, 'm': multiply}

    current_index = 0
    for number in args:
        current_operation = list(kwargs.keys())[current_index]

        if current_operation in mapper:
            result = mapper[current_operation](kwargs[current_operation], number)
            if result != None:
                kwargs[current_operation] = result

        current_index += 1

        if current_index == len(kwargs):
            current_index = 0

    return kwargs



print(math_operations(6, 2, 0, 0, 0, 1, a=0, s=1, d=1, m=2))