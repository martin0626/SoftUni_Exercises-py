events = input().split('|')
energy = 100
coins = 100
bankrupt = False
for event in events:
    action = event.split('-')
    act = action[0]
    energy_coins = int(action[1])

    if act == 'rest':
        if energy < 100:
            energy += energy_coins
            print (f'You gained {energy_coins} energy.\nCurrent energy: {energy}.')
        else:
            print (f'You gained 0 energy.\nCurrent energy: {energy}.')
    elif act == 'order':
        if energy >= 30:
            energy -= 30
            coins += energy_coins
            print (f'You earned {energy_coins} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= energy_coins:
            coins -= energy_coins

            print (f'You bought {act}.')
        else:
            bankrupt = True
            print (f'Closed! Cannot afford {act}.')
            break
    if energy > 100:
        energy = 100
if bankrupt == False:
    print (f'Day completed!\nCoins: {coins}\nEnergy: {energy}')



