import re

path = 'text.txt'


def replace_symbols(line):
    return re.sub(r'[-,.!?]', '@', line)


with open(path) as file:
    text = file.readlines()

current_line = 0

for l in text:
    if current_line % 2 == 0:
        l = replace_symbols(l)
        print(*list(reversed(l.split())))
    current_line += 1
