type1 = input()
char_1 = input()
char_2 = input()

def print_bigger (type, x, y):
    if type == 'int':
        if int(x) > int(y):
            result = x
        else:
            result = y
    elif type == 'char':
        if ord(x) > ord(y):
            result = x
        else:
            result = y
    else:
        if x > y:
            result = x
        else:
            result = y
    return result

print (print_bigger(type1, char_1, char_2))