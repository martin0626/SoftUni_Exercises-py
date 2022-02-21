text = input()
counter = {}

for digit in text:
    if digit != ' ':
        if digit not in counter and digit :
            counter[digit] = 0
        counter[digit] += 1

for value, key in counter.items():
    print (f'{value} -> {key}')

