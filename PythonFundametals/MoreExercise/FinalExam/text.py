username = input()

command_data = input()

while command_data != 'Sign up':
    command_data = command_data.split()

    command = command_data[0]

    if command == 'Case':
        if command_data[1] == 'lower':
            username = username.lower()

        else:
            username = username.upper()
        print (username)
    elif command == 'Reverse':
        start = int(command_data[1])
        end = int(command_data[2])
        if 0 <= start < len(username) and 0 <= end < len(username):
            reverse = username[start:end + 1][::-1]
            print (reverse)

    elif command == 'Cut':
        substring = command_data[1]
        if substring in username:
            username = username.replace(substring, '')
            print (username)
        else:
            print (f"The word {username} doesn't contain {substring}.")
        
    elif command == 'Replace':
        char = command_data[1]

        username = username.replace(char, '*')
        print (username)

    else:
        char_1 = command_data[1]
        if char_1 in username:
            print ('Vlaid')
        else:
            print (f'Your username must contain {char_1}.')
    command_data = input()