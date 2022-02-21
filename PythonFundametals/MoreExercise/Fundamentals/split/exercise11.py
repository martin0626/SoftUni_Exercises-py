veichels = input().split(', ')
n = int(input())
for x in range (n):
    commands = input().split(', ')
    if commands[0] == 'Add':
        if commands[1] in veichels:
            print ('Tank is already bought')
        else:
            print('Tank successfully bought')
            veichels.append(commands[1])
    elif commands[0] == 'Remove':
        if commands[1] in veichels:
            print ('Tank successfully sold')
            index = veichels.index(commands[1])
            veichels.pop(index)
        else:
            print ('Tank not found')
    elif commands[0] == 'Remove At':
        if int(commands[1]) <= len(veichels):
            veichels.pop(int(commands[1]))
            print ('Tank successfully sold')
        else:
            print ('Index out of range')
    elif commands[0] == 'Insert':
        if int(commands[1]) <= len(veichels):
            if commands[2] not in veichels:
                veichels.insert(int(commands[1]), commands[2])
                print ('Tank successfully bought')
            else:
                print ('Tank is already bought')

        else:
            print ('Index out of range')
print (', '.join(veichels))