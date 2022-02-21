rows, cols = [int(n) for n in input().split(', ')]
matrix = []
result = 0
for r in range(rows):
    row = [int(el) for el in input().split(', ')]
    matrix.append(row)
    result += sum(row)

print(result)
print(matrix)
