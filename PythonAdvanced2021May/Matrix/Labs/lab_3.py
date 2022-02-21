size = int(input())

matrix = []

result = 0

for r in range(size):
    matrix.append([int(n) for n in input().split()])
    result += matrix[r][r]

print(result)
