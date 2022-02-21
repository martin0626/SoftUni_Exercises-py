items = input().split(', ')
command = input().split(' - ')

while command[0] != 'Craft!':
    if command[0] == 'Collect':
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == 'Drop':
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == 'Combine Items':
        command2 = command[1].split(':')
        index1 = items.index(command2[0])
        if command2[0] in items:
            items.insert(index1 + 1, command2[1])
    else:
        if command[1] in items:
            items.append(items.pop(items.index(command[1])))
    command = input().split(' - ')

print(", ".join(items))

            

            

    