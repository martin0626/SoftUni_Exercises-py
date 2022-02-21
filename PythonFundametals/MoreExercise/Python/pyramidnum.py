n = int(input())

def pyramid_print (num):
    for i in range (1, num + 1):
        for j in range (1, i + 1):
            print (f'{j} ',end = '')
        print()
    for i in range (num - 1, 0, -1):
        for j in range (1, i +1):
            print (f'{j} ',end = '')
        print()


pyramid_print (n)