type = input ()
a = input ()
b = input()

def bigger (type, furst, second):
    result = None
    if type == 'int':
        if int (furst) > int (second):
           result = furst
        elif int (furst) < int (second):
            result = second

    elif  type == 'chr':
        if ord(furst) > ord (second):
            result = furst
        elif ord(furst) < ord (second):
            result = second
    else:
        if furst > second:
            result = furst
        elif furst < second:
            result = second
    return result

print (bigger(type, a, b))
        

    