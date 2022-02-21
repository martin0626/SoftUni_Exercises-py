size = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(size)]
secondary = 0

primary = 0

for r in range(size):
    primary += matrix[r][r]
    for c in range(size):
        if (r + c) == (size - 1):
            secondary += matrix[r][c]

print(abs(primary - secondary))
