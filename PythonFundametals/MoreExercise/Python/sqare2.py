a = int(input())

for i in range (1, a + 1):
    print (' ' * (a - i) + '*', end = '')
    for j in range (1, i):
        print ('-*', end='')
    print()

for i in reversed (range(1, a)):
    print (' ' * (a - i) + '*', end = '')
    for j in range (1, i):
        print ('-*', end='')
    print()