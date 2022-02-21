rows, cols = [int(n) for n in input().split(', ')]
matrix = [[int(el) for el in input().split(' ')]for _ in range(rows)]

for c in range(cols):
    result = 0
    for r in range(rows):
        result += matrix[r][c]
    print(result)
