rooms = int(input())
free_chairs = 0
game_off = False
for room in range (1, rooms + 1):
    room_condition = input().split()
    chairs, people = room_condition
    if len(chairs) >= int(people):
        free_chairs += len(chairs) - int(people)
    else:
        print (f'{int(people) - len(chairs)} more chairs needed in room {room}')
        game_off = True
if game_off == False:
    print (f'Game On, {free_chairs} free chairs left')

