number = int(input())

def loading_bar (num):
    num = num // 10
    a = '[' + '%' * num + '.' * (10 - num) + ']'
    if not num * 10 == 100:
        print (f'{num * 10}% {a}\nStill loading...')
    else:
        print (f'100% Complete!\n{a}')
loading_bar(number)