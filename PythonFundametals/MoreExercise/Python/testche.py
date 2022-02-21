n = int(input())


for x in range (1, n + 1):
    print ( ' ' * n + ( '*' * x) + n * ' ')
    if x == n:
        print ( ' ' * n + ( '*' * (x+1)) + n * ' ')
for x in range (n, 0, -1):
    print (' ' * n + ( '*' * x) + n * ' ')
