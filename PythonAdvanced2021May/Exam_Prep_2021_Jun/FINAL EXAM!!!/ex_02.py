def is_valid(r, c):
    return 0 <= r < 5 and 0 <= c < 5


def shoot_up(row, col):
    global field, shots, size
    current_row = row
    while True:
        current_row -= 1
        if not is_valid(current_row, col):
            break

        if field[current_row][col] == 'x':
            shots.append([current_row, col])
            field[current_row][col] = '.'
            return


def shoot_down(row, col):
    global field, shots, size
    current_row = row
    while True:
        current_row += 1
        if not is_valid(current_row, col):
            break

        if field[current_row][col] == 'x':
            shots.append([current_row, col])
            field[current_row][col] = '.'
            return


def shoot_left(row, col):
    global field, shots, size
    current_col = col
    while True:
        current_col -= 1
        if not is_valid(row, current_col):
            break

        if field[row][current_col] == 'x':
            shots.append([row, current_col])
            field[row][current_col] = '.'
            return


def shoot_right(row, col):
    global field, shots, size
    current_col = col
    while True:
        current_col += 1
        if not is_valid(row, current_col):
            break

        if field[row][current_col] == 'x':
            shots.append([row, current_col])
            field[row][current_col] = '.'
            return


def current_pos():
    global field, size
    for r in range(size):
        for c in range(size):
            if field[r][c] == 'A':
                return [r, c]


def cells_counter():
    global size, field
    result = 0
    for r in range(size):
        result += field[r].count('x')
    return result


size = 5

field = [input().split() for el in range(5)]
shots = []
n = int(input())

directions_mapper = {'up': shoot_up, 'down': shoot_down, 'left': shoot_left, 'right': shoot_right}
move_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(n):
    if cells_counter() == 0:
        break

    command = input()
    row_shooter, col_shooter = current_pos()

    if command.startswith('shoot'):
        direction = command.split()[1]
        if direction in directions_mapper:
            directions_mapper[direction](row_shooter, col_shooter)

    elif command.startswith('move'):
        move_direction = command.split()[1]
        if len(command.split()) == 3:
            steps = int(command.split()[2])
        else:
            steps = 0

        if move_direction in move_mapper:
            row_to_move = (move_mapper[move_direction][0] * steps) + row_shooter
            col_to_move = (move_mapper[move_direction][1] * steps) + col_shooter
            if is_valid(row_to_move, col_to_move):
                if field[row_to_move][col_to_move] == '.':
                    field[row_to_move][col_to_move] = 'A'
                    field[row_shooter][col_shooter] = '.'


if cells_counter() > 0:
    print(f'Training not completed! {cells_counter()} targets left.')

else:
    print(f'Training completed! All {len(shots)} targets hit.')

[print(s) for s in shots]
