operator = input()
furst_num = int(input())
second_num = int(input())

def operation (oper, x, y):
    result = 0
    if oper == 'multiply':
        result = x * y
    elif oper == 'divide':
        result = x // y
    elif oper == 'add':
        result = x + y
    else:
        result = x - y

    return result
print (operation(operator, furst_num, second_num))
