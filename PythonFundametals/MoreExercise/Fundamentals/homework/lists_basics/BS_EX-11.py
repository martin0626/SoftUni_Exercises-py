num = int(input())

for x in range (1, num + 1):
    sum_all = 0
    x = str(x)
    special = False
    if int(x) < 10 and (int(x) == 5 or int(x) == 7 or int(x) == 11):
        special = True
    if int(x) > 10:
        for n in x:
            sum_all += int(n)
        if sum_all == 5 or sum_all == 7 or sum_all == 11:
            special = True
    print (f'{x} -> {special}')

        
    
    
    
    


