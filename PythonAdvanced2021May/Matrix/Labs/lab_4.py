def symbol_finder(matrix_size, m, symbol_find):
    for r in range(matrix_size):
        for c in range(matrix_size):
            if m[r][c] == symbol_find:
                coordinates = (r, c)
                print(coordinates)
                return
    print(f'{symbol_find} does not occur in the matrix')


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

symbol = input()
symbol_finder(size, matrix, symbol)
