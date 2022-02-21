def print_field(matrix):
    [print(''.join(line)) for line in matrix]


def find_pos(r, c, matrix):
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'P':
                return [i, j]


def is_valid(r, c, size_r, size_c):
    return 0 <= r < size_r and 0 <= c < size_c


def bunnies_move(matrix, cur_r, cur_c, rows_field, cols_field):
    is_dead = None
    rows_add = [1, 0, 0, -1]
    cols_add = [0, 1, -1, 0]
    for i in range(4):
        r = cur_r + rows_add[i]
        c = cur_c + cols_add[i]
        if is_valid(r, c, rows_field, cols_field):
            if matrix[r][c] == 'P':
                is_dead = True

            elif matrix[r][c] != 'B':
                matrix[r][c] = '&'
    return matrix, is_dead


def next_move(matrix, r_size, c_size):
    is_dead = False

    for r in range(r_size):
        for c in range(c_size):
            if matrix[r][c] == 'B':
                matrix, die = bunnies_move(matrix, r, c, r_size, c_size)
                if die:
                    is_dead = True

    for r in range(r_size):
        for c in range(c_size):
            if matrix[r][c] == '&':
                matrix[r][c] = 'B'

    return matrix, is_dead


rows, cols = [int(n) for n in input().split()]

field = [[el for el in input()] for _ in range(rows)]

commands = [c for c in input()]

dead = False

win = False


dead_row = 0
dead_col = 0

for command in commands:
    row_p, col_p = find_pos(rows, cols, field)

    if command == 'L':

        if is_valid(row_p, col_p - 1, rows, cols):
            field[row_p][col_p] = '.'
            if field[row_p][col_p - 1] == 'B':
                dead = True
                dead_row, dead_col = row_p, col_p - 1
            else:
                field[row_p][col_p - 1] = 'P'
        else:
            win = True
            field[row_p][col_p] = '.'

    elif command == 'R':

        if is_valid(row_p, col_p + 1, rows, cols):
            field[row_p][col_p] = '.'
            if field[row_p][col_p + 1] == 'B':
                dead = True
                dead_row, dead_col = row_p, col_p + 1
            else:
                field[row_p][col_p + 1] = 'P'
        else:
            win = True
            field[row_p][col_p] = '.'

    elif command == 'U':

        if is_valid(row_p - 1, col_p, rows, cols):
            field[row_p][col_p] = '.'
            if field[row_p - 1][col_p] == 'B':
                dead = True
                dead_row, dead_col = row_p - 1, col_p
            else:
                field[row_p - 1][col_p] = 'P'

        else:
            win = True
            field[row_p][col_p] = '.'

    elif command == 'D':

        if is_valid(row_p + 1, col_p, rows, cols):
            field[row_p][col_p] = '.'
            if field[row_p + 1][col_p] == 'B':
                dead = True
                dead_row, dead_col = row_p + 1, col_p
            else:
                field[row_p + 1][col_p] = 'P'
        else:
            win = True
            field[row_p][col_p] = '.'

    if dead:
        field, dead = next_move(field, rows, cols)
        dead = True

    else:
        field, dead = next_move(field, rows, cols)

    if win:
        print_field(field)
        print(f'won: {row_p} {col_p}')
        exit(0)

    if dead:
        try:
            dead_row, dead_col = find_pos(rows, cols, field)
            field[dead_row][dead_col] = "B"
        except TypeError:
            pass

        print_field(field)
        print(f'dead: {dead_row} {dead_col}')
        exit(0)


