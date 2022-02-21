rooms = input().split('|')

health = 100
bitcoin = 0

rooms_count = 0
death = False
for x in rooms:
    room_in = x.split()
    rooms_count += 1
    if room_in[0] == 'potion':
        if health < 100:
            health += int(room_in[1])
            if health > 100:
                health = 100
        print (f'You healed for {room_in[1]}\nCurrent health: {health} hp.')

    elif room_in[0] == 'chest':
        bitcoin += int(room_in[1])
        print (f'You found {room_in[1]} bitcoins.')
    else:
        health -= int(room_in[1])
        if health <= 0:
            print (f'You died! Killed by {room_in[0]}.\nBest room: {rooms_count}')
            death = True
            break
        else:
            print (f'You slayed {room_in[0]}.')

if death == False:
    print (f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")