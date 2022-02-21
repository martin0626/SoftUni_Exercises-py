gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    if command[0] == 'OutOfStock':
        for y in gifts:
            if command[1] == y:
                index = gifts.index(command[1])
                gifts[index] = None  
    elif command[0] == 'Required':
        if int(command[2]) <= len(gifts):
            gifts[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    command = input()
for x in gifts:
    if x != None:
        print (x, end = ' ')