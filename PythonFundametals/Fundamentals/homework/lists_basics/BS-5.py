num = int(input())

for x in range (1, num + 1):
    for y in range (1, num + 1):
        print ('*' * y)
        if y == num:
            break
    break
for x in range (num - 1, -1, -1):
    for y in range (num -1, -1, -1):
        print ('*' * y)
        if y == 0:
            break
    break
        