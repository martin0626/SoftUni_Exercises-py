rows, cows = [int(n) for n in input().split(', ')]

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

max_sum = 0
coordinates = None

for r in range(rows - 1, 0, -1):
    for c in range(cows - 1, 0, -1):
        current_sum = matrix[r][c] + matrix[r][c - 1] + matrix[r - 1][c] + matrix[r - 1][c - 1]
        if max_sum <= current_sum:
            max_sum = current_sum
            coordinates = [r, c]
r, c = coordinates
print(f'{matrix[r - 1][c - 1]} {matrix[r - 1][c]}\n{matrix[r][c - 1]} {matrix[r][c]}')
print(max_sum)
