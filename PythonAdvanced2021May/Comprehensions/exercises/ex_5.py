size = int(input())
matrix = [[int(n) for n in input().split(', ')] for _ in range(size)]

first_d = [matrix[r][r] for r in range(size)]
print(f'First diagonal: {", ".join([str(el) for el in first_d])}. Sum: {sum(first_d)}')

second_d = [matrix[r][c] for r in range(size) for c in range(size) if (r + c) == (size - 1)]
print(f'Second diagonal: {", ".join([str(el) for el in second_d])}. Sum: {sum(second_d)}')
