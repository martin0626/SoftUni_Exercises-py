contenders = int(input())
total_bakes = 0 
total_charity = 0
for x in range (contenders):
    name = input()
    type_sweets = input()
    cookies_n = 0
    cake_n = 0
    waffles_n = 0
    while type_sweets != 'Stop baking!':
        num = int(input())
        total_bakes += num
       
        if type_sweets == 'cookies':
            total_charity += num * 1.5
            cookies_n += num 
            
        elif type_sweets == 'cakes':
            total_charity += num * 7.8
            cake_n += num

        elif type_sweets == 'waffles':
            total_charity += num * 2.3
            waffles_n += num

        type_sweets = input()
    print (f'{name} baked {cookies_n} cookies, {cake_n} cakes and {waffles_n} waffles.')
print (f'All bakery sold: {total_bakes}\nTotal sum for charity: {total_charity:.2f} lv.')