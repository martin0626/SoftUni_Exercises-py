def flights(*args):
    result = {}
    for i in range(len(args)):
        if args[i] == 'Finish':
            break

        elif isinstance(args[i], int):
            result[args[i - 1]] += args[i]

        else:
            if args[i] not in result:
                result[args[i]] = 0
    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
