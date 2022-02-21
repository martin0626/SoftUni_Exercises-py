first_set_len, second_set_len = [int(n) for n in input().split()]

first_set = set([input() for _ in range(first_set_len)])
second_set = set([input() for _ in range(second_set_len)])

[print(el) for el in first_set.intersection(second_set)]
