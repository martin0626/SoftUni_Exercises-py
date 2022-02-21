messages = []

command = input()

while command != 'end':
    command = command.split()

    if command[0] == 'Chat':
        messages.append(command[1])

    elif command[0] == 'Delete' and command[1] in messages:
        messages.remove(command[1])

        
    elif command[0] == 'Edit':
        index = messages.index(command[1])
        messages[index] = command[2]
        
    elif command[0] == 'Pin':
        index = messages.index(command[1])
        msg = messages.pop(index)
        messages.append(msg)
    elif command[0] == 'Spam':
        for message in command:
            if message != 'Spam':
                messages.append(message)
    command = input()

print ('\n'.join(messages))
        
        