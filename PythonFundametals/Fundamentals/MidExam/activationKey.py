activation_key = input()

command = input()

while command != 'Generate':
    command = command.split('>>>')
    if command[0] == 'Contains':
        if command[1] in activation_key:
            print (f'{activation_key} contains {command[1]}')
        else:
            print ('Substring not found!')
    elif command[0] == 'Flip':
        if command [1] == 'Upper':
            up = activation_key[int(command[2]):int(command[3])].upper()
            activation_key = activation_key.replace(activation_key[int(command[2]):int(command[3])], up)
        elif command[1] == 'Lower':
            lower = activation_key[int(command[2]):int(command[3])].lower()
            activation_key = activation_key.replace(activation_key[int(command[2]):int(command[3])], lower)
        print (activation_key)
    elif command[0] == 'Slice':
        to_del = activation_key[int(command[1]):int(command[2])]
        activation_key = activation_key.replace(to_del, '')
        print (activation_key)
    command = input()
print (f'Your activation key is: {activation_key}')




            