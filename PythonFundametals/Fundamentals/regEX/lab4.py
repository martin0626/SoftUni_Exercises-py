import re

numbers = input()

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

result = re.finditer(pattern, numbers)

result = [x.group() for x in result]

print (*result)