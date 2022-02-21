names = input().split(', ')
result = {n: len(n) for n in names}

print(', '.join([f'{name} -> {length}' for name, length in result.items()]))
