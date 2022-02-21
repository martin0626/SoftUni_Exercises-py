size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size)]

while True:
    command = input()
    if command == 'END':
        [print(' '.join([str(n) for n in r])) for r in matrix]
        break

    if command.startswith('Add'):
        row, col, num_add = command.split()[1::]
        if 0 <= int(row) < size and 0 <= int(col) < size:
            matrix[int(row)][int(col)] += int(num_add)
        else:
            print('Invalid coordinates')

    else:
        row, col, num_add = command.split()[1::]
        if 0 <= int(row) < size and 0 <= int(col) < size:
            matrix[int(row)][int(col)] -= int(num_add)
        else:
            print(f'Invalid coordinates')
