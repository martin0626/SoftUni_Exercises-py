deck = input().split(':')
command = input().split()
new = []
while command[0] != 'Ready':
    if command[0] == 'Add':
        if command[1]  not in deck :
            print("Card not found!")
        else:
            new.append(command[1])
            deck.append(deck.pop(deck.index(command[1])))
            
    elif command[0] == 'Insert':
        if command[1] not in deck or int(command[2]) > len(deck):
            print("Error!")
        else:
            new.append(command[1])
            deck.remove(command[1])
            deck.insert(int(command[2]), command[1])
    elif command[0] == 'Remove':
        if command[1]  not in deck :
            print("Card not found!")
        else:
            deck.remove(command[1])

    elif command[0] == 'Swap':
        index1 = deck.index(command[1])
        index2 = deck.index(command[2])
        deck[index1], deck[index2] = deck[index2], deck[index1]
    else:
        deck.reverse()
    
    command = input().split()


for x in deck:
    if x in new:
        print (x, end = ' ')      