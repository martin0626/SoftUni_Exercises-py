items = input().split()
materials_other = {}

legendary = ['Shards', 'Fragments', 'Motes']
for index in range (0, len(items), 2):
    key = items[index + 1].lower()
    value = int(items[index])
    
    
    if key not in materials_other:
        materials_other[key] = 0
    materials_other[key] += value
    

for k, v in sorted(materials_other.items()):
    k = k.lower()
    if v >= 250:
        materials_other[k] -= 250
        if k == 'shards':
            legend = 'Shadowmourne'
        elif k == 'fragments':
            legend = 'Valanyr'
        else:
            legend = 'Dragonwarth'
        
        print (f'{legend} obtained!')
    
materials_other = dict(sorted(materials_other.items(), key=lambda x: x[1], reverse=True))
for k, v in sorted(materials_other.items()):
    
    if key in legendary:
        print (f'{k}: {v}')

for k, v in sorted(materials_other.items()):
    if key not in legendary:
        print (f'{k}: {v}')