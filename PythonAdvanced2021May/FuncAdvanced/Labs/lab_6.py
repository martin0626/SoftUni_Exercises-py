from itertools import permutations
characters = [e for e in input()]
[print(*t, sep='') for t in list(permutations(characters))]
