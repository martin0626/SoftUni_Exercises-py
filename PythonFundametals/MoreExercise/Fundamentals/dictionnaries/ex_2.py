items = {}

command = input()
num = 1

while command != 'stop':
    

    if num % 2 != 0:
        last_item = command   
        if command not in items:
            items[command] = 0

    else:
        items[last_item] += int(command)
    command = input()
    num += 1
for key, value in items.items():
    print (f'{key} -> {value}')
