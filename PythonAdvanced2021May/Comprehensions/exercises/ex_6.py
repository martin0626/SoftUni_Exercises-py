alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

rows, cols = [int(n) for n in input().split()]
matrix = [[f'{alphabet[r]}{alphabet[r + c]}{alphabet[r]}' for c in range(cols)] for r in range(rows)]
[print(' '.join(r)) for r in matrix]
