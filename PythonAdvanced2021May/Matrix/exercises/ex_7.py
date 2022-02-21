def matrix_print(m):
    for row in m:
        print(' '.join([str(el) for el in row]))


def is_valid(r, c, s):
    return 0 <= r < s and 0 <= c < s


def explosion(mat, cur_r, cur_c, s):
    rows_add = [-1, 1, 0, 0, 1, 1, -1, -1]
    cols_add = [0, 0, 1, -1, -1, 1, 1, -1]
    for i in range(8):
        r = cur_r + rows_add[i]
        c = cur_c + cols_add[i]
        if is_valid(r, c, s) and matrix[r][c] > 0 and matrix[cur_r][cur_c] > 0:
            matrix[r][c] -= matrix[cur_r][cur_c]
    if matrix[cur_r][cur_c] > 0:
        matrix[cur_r][cur_c] = 0

    return mat


size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size)]

commands = [[int(c) for c in command.split(',')] for command in input().split()]

for cmd in commands:

    r_explosion, c_explosion = cmd
    matrix = explosion(matrix, r_explosion, c_explosion, size)

active_cells = 0
sum_active = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            sum_active += matrix[r][c]
            active_cells += 1

print(f'Alive cells: {active_cells}\nSum: {sum_active}')
matrix_print(matrix)
