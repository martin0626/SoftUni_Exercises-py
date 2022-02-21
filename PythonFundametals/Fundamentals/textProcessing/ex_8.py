string = input().split()
results = []


def number (text):
    result = ''
    for x in text:
        if x.isdigit():
            result += x

    return int(result)


for combination in string:
    current_number = number(combination)
    result = 0
    if combination[0].isupper():
        position = ord(combination[0]) - 64
        result += current_number/position
    elif combination[0].islower():
        position = ord(combination[0]) - 96
        result += position * current_number
    
    if combination[-1].isupper():
        position = ord(combination[-1]) - 64
        result -= position
    elif combination[-1].islower():
        position = ord(combination[-1]) - 96
        result += position
        
    results.append(result)
    result = 0


print (f'{sum(results):.2f}')



