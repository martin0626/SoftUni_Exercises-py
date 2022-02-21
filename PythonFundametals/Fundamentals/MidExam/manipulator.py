friends = input().split(', ')
blacklisted = 0
lost = 0
command = input()
def inside (list_1, item):
    for it in list_1:
        if it == item:
            return True
    return  False


while command != 'Report':
    command = command.split()
    if command[0] == 'Blacklist':
        if inside(friends, command[1]):
            index = friends.index(command[1])
            print (f'{friends[index]} was blacklisted.')
            friends[index] = 'Blacklisted'
            blacklisted += 1
        else:
            print (f'{command[1]} was not found.')
            
    elif command[0] == 'Error':
        index = int(command[1])
        if friends[index] != 'Blacklisted' and friends[index] != 'Lost':
            print (f'{friends[index]} was lost due to an error.')
            friends[index] = 'Lost'
            lost += 1

    elif command[0] == 'Change' and 0 <= int(command[1]) < len(friends):
        print (f'{friends[int(command[1])]} changed his username to {command[2]}.')
        friends[int(command[1])] = command[2]


    command = input()
print (f'Blacklisted names: {blacklisted}\nLost names: {lost}')
print (' '.join(friends))

