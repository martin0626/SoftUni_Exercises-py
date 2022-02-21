n = int(input())
register = {}
for x in range (1, n + 1):
    command = input().split()

    if command[0] == 'register':
        username = command[1]
        license_number = command[2]
        if username not in register:
            register[username] = license_number
            print (f'{username} registered {license_number} successfully')
        else:
            print (f'ERROR: already registered with plate number {license_number}')

    else:
        username = command[1]

        if username in register:
            register.pop(username)
            print (f'{username} unregistered successfully')
        else:
            print (f'ERROR: user {username} not found')




for key, value in register.items():
    print (f'{key} => {value}')



