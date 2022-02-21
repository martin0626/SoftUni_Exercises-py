def is_true(row, col, size_to_check):
    return 0 <= row < size_to_check and 0 <= col < size_to_check


def knight_move(mate, cur_r, cur_c, s):
    knights_in_range = 0
    rows_to_move = [-2, -2, -1, -1, 1, 1, 2, 2]
    cols_to_move = [-1, 1, -2, 2, -2, 2, -1, 1]
    for i in range(8):
        r = cur_r + rows_to_move[i]
        c = cur_c + cols_to_move[i]
        if is_true(r, c, s) and mate[r][c] == 'K':
            knights_in_range += 1
    return knights_in_range


size = int(input())

matrix = [[el for el in input()] for _ in range(size)]

kills = 0

while True:

    hardest_knight = 0
    coordinates = []

    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'K':
                current_hits = knight_move(matrix, r, c, size)
                if current_hits > hardest_knight:
                    hardest_knight = current_hits
                    coordinates = [r, c]
    if hardest_knight == 0:
        print(kills)
        break

    else:
        kills += 1
        i, j = coordinates
        matrix[i][j] = 'O'
