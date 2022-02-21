num = int(input())
current = 1
bigger_n = False
for row in range (1, num + 1):
    for cow in range (1, row + 1):
        if current > num:
            bigger_n = True 
            break
        print (str(current) + ' ', end = '')
        current += 1
    if bigger_n:
        break
    print ()                                        