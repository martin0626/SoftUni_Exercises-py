x = int(input())
booleva = False

current = 1
for y in range (1, x + 1):
    for i in range (1, y+1):
        if current > x:
            booleva = True
            break
        print (str(current) + '', end ='')
        current += 1
        
    if booleva:
        break
    print ()


