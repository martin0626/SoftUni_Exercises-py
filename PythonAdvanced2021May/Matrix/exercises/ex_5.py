def matrix_print(m):
    current_row = 1
    for row in m:
        if current_row % 2 == 0:
            print(''.join(reversed([str(el) for el in row])))

        else:
            print(''.join([str(el) for el in row]))

        current_row += 1


rows, cols = [int(n) for n in input().split()]
matrix = [[0 for _ in range(cols)]for _ in range(rows)]
snake = input()
current_index = 0
for r in range(rows):
    for c in range(cols):
        matrix[r][c] = snake[current_index]
        current_index += 1
        if current_index == len(snake):
            current_index = 0

matrix_print(matrix)



