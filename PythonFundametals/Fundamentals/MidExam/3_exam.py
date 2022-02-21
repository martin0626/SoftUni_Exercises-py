cards = input().split(':')
new_cards = []
command = input()

while command != 'Ready':
    command = command.split()

    if command[0] == 'Add':
        if  command[1] in cards:
            new_cards.append(command[1])
        else:
            print ('Card not found.')
        
    elif command[0] == 'Insert':
        if 0 <= int(command[2]) < len(new_cards) and command[1] in cards:
            new_cards.insert(int(command[2]), command[1])
        else:
            print ('Error!')

    elif command[0] == 'Remove':
        if command[1] in new_cards:
            new_cards.remove(command[1])
        else:
            print ('Card not found.')
        

    elif command[0] == 'Swap':
        index_1 = new_cards.index(command[1])
        index_2 = new_cards.index(command[2])
        new_cards[index_1], new_cards[index_2] = new_cards[index_2], new_cards[index_1]



    elif command[0] == 'Shuffle':
        new_cards.reverse()


    command = input()
print (' '.join(new_cards))
