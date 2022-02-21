plants = {}

n = int(input())

for _ in range (n):
    plant, rarity = input().split('<->')

    if plant not in plants:
        plants[plant] = {'rarity':0, 'rating': 0, 'num': 0}
    plants[plant]['rarity'] = int(rarity)

command_date = input()

while not command_date == 'Exhibition':
    command_date = [x for x in command_date.split() if x != '-']
    command = command_date[0]

    if command == 'Rate:':
        
        plant_to_rate = command_date[1]
        rating = float(command_date[2])
        if plant_to_rate in plants:
            plants[plant_to_rate]['rating'] += rating
            plants[plant_to_rate]['num'] += 1
        else:
            print ('error')

    elif command == 'Update:':
        plant_to_update = command_date[1]
        new_rarity = command_date[2]
        if plant_to_update in plants:
            plants[plant_to_update]['rarity'] = int(new_rarity)
        else:
            print ('error')
            
    else:
        plant_reset = command_date[1]
        if plant_reset in plants:
            plants[plant_reset]['rating'] = 0
            plants[plant_reset]['num'] = 0
        else:
            print ('error')

    
    command_date = input()
print ('Plants for the exhibition:')

plants = dict(sorted(plants.items(), key = lambda x: (-x[1]['rarity'], -x[1]['rating'])))
for plant in plants.keys():
    if plants[plant]['rating'] != 0:
        average = plants[plant]['rating'] / plants[plant]['num']
    else:
        average = 0
    print (f'- {plant}; Rarity: {plants[plant]["rarity"]}; Rating: {average:.2f}')
        
