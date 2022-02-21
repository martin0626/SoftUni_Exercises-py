friends = input().split(', ')
command = input().split()
blck = 0
lost = 0
while command[0] != 'Report':
    if command[0] == 'Blacklist':
        if command[1] in friends:
            print (f'{command[1]} was blacklisted.')
            index1 = friends.index(command[1])
            friends[index1] = 'Blacklisted'
            blck += 1
        else:
            print (f'{command[1]} was not found.')

    elif command[0] == 'Error':
        if friends[int(command[1])] == 'Blacklisted' or friends[int(command[1])] == 'Lost':
            pass
        else:
            print (f'{friends[int(command[1])]} was lost due to an error.')
            #index1 = friends.index(int(command[1]))
            friends[int(command[1])] = 'Lost'
            lost += 1
        

    else:
        if int(command[1]) <= len(friends):
            
            print (f'{friends[int(command[1])]} changed his username to {command[2]}.')
            friends[int(command[1])] = command[2]
    command = input().split()
print (f'Blacklisted names: {blck}\nLost names: {lost}')
print (' '.join(friends))


