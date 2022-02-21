furst =  int(input())
second = int(input())
point = int (input())
left = min (furst, second)
right = max (furst, second)

if point >= left and point <= right:
    print ('in')
    furst -= point
    second -= point
    if abs(furst) < abs(second):
        print (abs(furst))
    else: 
        print (abs(second))

else:
    print ('out')
    furst -= point
    second -= point
    if abs(furst) < abs(second):
        print (abs(furst))
    else: 
        print (abs(second))
