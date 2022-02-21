import re


pattern = re.compile(r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))')
input_1 = input()
search = re.finditer(pattern, input_1)

for match in search:
    print (match.group(0), end = ' ')

