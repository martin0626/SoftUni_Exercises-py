n = int(input())

names = set([input() for _ in range(n)])
[print(n) for n in names]
