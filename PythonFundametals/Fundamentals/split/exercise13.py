num = int(input())

def pyramid (n):
    for x in range (1, n + 1):
        for j in range (1, x + 1):
            print (j, end = ' ')
        print()
    for x in range (n - 1, 0, -1):
        for j in range (1, x + 1):
            print (j, end = ' ')
        print ()
pyramid(num)