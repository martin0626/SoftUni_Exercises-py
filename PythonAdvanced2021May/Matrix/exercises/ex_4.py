def matrix_print(m):
    for row in m:
        print(' '.join([str(el) for el in row]))


rows, cols = [int(n) for n in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

while True:
    command = input()

    if command == 'END':
        break

    if command.startswith('swap') and len(command.split()) == 5:
        r_1, c_1, r_2, c_2 = [int(el) for el in command.split()[1::]]

        try:
            el = matrix[r_1][c_1]
            matrix[r_1][c_1] = matrix[r_2][c_2]
            matrix[r_2][c_2] = el
            matrix_print(matrix)
        except IndexError:
            print('Invalid input!')

    else:
        print('Invalid input!')


