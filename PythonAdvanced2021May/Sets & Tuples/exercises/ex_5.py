command = input()
names_numbers = {}
n = 0
while True:
    try:
        name, number = command.split('-')
        names_numbers[name] = number
        command = input()
    except ValueError:
        n = int(command)
        break


for _ in range(n):
    name = input()

    if name in names_numbers.keys():
        print(f'{name} -> {names_numbers[name]}')
    else:
        print(f'Contact {name} does not exist.')
