rows = int(input())

print([int(n) for _ in range(rows) for n in input().split(', ')])
