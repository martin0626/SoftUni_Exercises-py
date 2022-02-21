junks = {}
special = {'fragments': 0, 'shards': 0, 'motes': 0}

def who_win (special_tems):
    for v, k in special_tems.items():
        if k >= 250:
            if v == 'shards':
                return 'Shadowmourne obtained!'
            elif v == 'fragments':
                return 'Valanyr obtained!'
            return 'Dragonwrath obtained!'
    
while True:
    brk = False
    items = input().split()
    for index in range(0, len(items), 2):
        key = items[index + 1].lower()
        value = int(items[index])

        if key in special:
            special[key] += value
        
        else:
            if not key in junks:
                junks[key] = 0
            junks[key] += value
        if who_win(special) != None:
            print (who_win(special))
            brk = True
       
            
            break
    if brk == True:
        break
        
for key, value in special.items():
    if special[key] >= 250:
        special[key] -= 250

items_values_special = set(special.values())

if len == len(items_values_special) == len(special):
    special = special = dict(sorted(special.items(), key=lambda item: -item[1]))

else:
    special = dict(sorted(special.items(), key=lambda item: (-item[1], item[0])))

for key, value in special.items():
    
    print (f'{key}: {value}')


junks = dict(sorted(junks.items(), key=lambda item: item[0]))

for key, value in junks.items():
    print (f'{key}: {value}')







