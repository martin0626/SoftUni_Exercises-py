def is_square(matrix_1, curr_r, curr_c):
    return matrix_1[curr_r][curr_c] == \
           matrix_1[curr_r][curr_c + 1] == \
           matrix_1[curr_r + 1][curr_c] == \
           matrix_1[curr_r + 1][curr_c + 1]


rows, cols = [int(i) for i in input().split(' ')]
matrix = [[el for el in input().split()] for _ in range(rows)]

square_elements = []

for r in range(rows - 1):
    for c in range(cols - 1):
        if is_square(matrix, r, c):
            square_elements.append([r, c])

print(len(square_elements))
