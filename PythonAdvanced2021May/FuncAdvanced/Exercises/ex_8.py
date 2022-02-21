def even_odd(*args):
    command = args[-1]
    nums = list(map(int, args[:-1]))
    if command == 'odd':
        odd_nums = list(filter(lambda x: x % 2 != 0, nums))
        return odd_nums

    else:
        even_nums = list(filter(lambda x: x % 2 == 0, nums))
        return even_nums


print(even_odd(1, 2, 3, 4, 5, 6, "odd"))
