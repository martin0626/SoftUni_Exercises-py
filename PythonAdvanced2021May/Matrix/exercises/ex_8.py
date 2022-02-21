def is_valid(r, c, s):
    return 0 <= r < s and 0 <= c < s


def miner_position(matrix, s):
    for r in range(s):
        for c in range(s):
            if matrix[r][c] == 's':
                return [r, c]


def is_coals_left(matrix, s):
    for r in range(s):
        for c in range(s):
            if matrix[r][c] == 'c':
                return True
    return False


def checker(matrix, r, c, curr_coals, end_bool):
    if matrix[r][c] == 'c':
        curr_coals += 1

    elif matrix[r][c] == 'e':
        end_bool = True

    # matrix[r][c] = '*'
    return matrix, curr_coals, end_bool


def all_coals(matrix, s):
    coal_left = 0
    for r in range(s):
        for c in range(s):
            if matrix[r][c] == 'c':
                coal_left += 1
    return coal_left


size = int(input())
commands = input().split()
field = [[el for el in input().split()] for _ in range(size)]

coals = 0
is_end = False
current_index = 0

for command in commands:
    current_row, current_col = miner_position(field, size)

    if command == 'up':
        r_move = current_row - 1
        c_move = current_col
        if is_valid(r_move, c_move, size):
            field, coals, is_end = checker(field, r_move, c_move, coals, is_end)
            field[current_row][current_col] = '*'
            field[r_move][c_move] = 's'

    elif command == 'down':
        r_move = current_row + 1
        c_move = current_col
        if is_valid(r_move, c_move, size):
            field, coals, is_end = checker(field, r_move, c_move, coals, is_end)
            field[current_row][current_col] = '*'
            field[r_move][c_move] = 's'

    elif command == 'left':
        r_move = current_row
        c_move = current_col - 1
        if is_valid(r_move, c_move, size):
            field, coals, is_end = checker(field, r_move, c_move, coals, is_end)
            field[current_row][current_col] = '*'
            field[r_move][c_move] = 's'

    elif command == 'right':
        r_move = current_row
        c_move = current_col + 1
        if is_valid(r_move, c_move, size):
            field, coals, is_end = checker(field, r_move, c_move, coals, is_end)
            field[current_row][current_col] = '*'
            field[r_move][c_move] = 's'

    if not is_coals_left(field, size):
        r_now, c_now = miner_position(field, size)
        print(f'You collected all coals! ({r_now}, {c_now})')
        break

    if is_end:
        r_now, c_now = miner_position(field, size)
        print(f'Game over! ({r_now}, {c_now})')
        break

    if current_index == (len(commands) - 1):
        r_now, c_now = miner_position(field, size)
        c_left = all_coals(field, size)
        print(f'{c_left} coals left. ({r_now}, {c_now})')

    current_index += 1
