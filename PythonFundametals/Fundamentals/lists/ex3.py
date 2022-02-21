a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

cards = input()
spl = cards.split()

for x in spl:
    card = x.split('-')
    number = int(card[1])
    if card[0] == 'A':
        
        if number in a:
            a.remove(number)
        else:
            continue
            
    if card[0] == 'B':
        
        if number in b:
            b.remove(number)
        else:
            continue

if len(a) >= 7 and len(b) >= 7:        
    print (f'Team A - {len(a)}; Team B - {len(b)}')
else:
    print (f'Team A - {len(a)}; Team B - {len(b)}\nGame was terminated')
