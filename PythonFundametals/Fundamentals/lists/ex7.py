gifts = input()
list_1 = gifts.split()
commands = input()

while commands != 'No Money':
    command_one = commands.split()

    if command_one[0] == 'OutOfStock':
        for index, item in enumerate(list_1):
            if item == command_one[1]:
                list_1[index] = None
    if command_one[0] == 'Required':
        num = int(command_one[2])
        if num <= (len(list_1) - 1) and num >= 0:
            list_1[num] = command_one[1]

    if command_one[0] == 'JustInCase':
        list_1[-1] = command_one[1]

    commands = input()

for x in list_1:
    if x != None:
        print(x, end = ' ')

