aim = [int(x) for x in input().split('|')]

commands = input()
points = 0
while commands != 'Game over':
    commands = commands.split('@')
    index = None
    
    
    if commands[0] == 'Shoot Left' and 0 <= int(commands[1]) < len(aim):
        index = int(commands[1]) - int(commands[2])
        while (-1 * index) > len(aim):
            index += len(aim)

    elif commands[0] == 'Shoot Right' and 0 <= int(commands[1]) < len(aim):
        index = int(commands[1]) + int(commands[2])
        while index >= len(aim):
            index -= len(aim)
    elif commands[0] == 'Reverse':
        aim.reverse()
    
    if index != None:
        if aim[index] >= 5:
            aim[index] -= 5
            points += 5
        else:
            points += aim[index]
            aim[index] = 0
    commands = input()
        
print (' - '.join(list(map(str, aim))))
print (f'Iskren finished the archery tournament with {points} points!')






    