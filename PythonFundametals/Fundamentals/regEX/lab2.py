import re
text = input()

pattern = r'\+359(\s-)2\1\d{3}\1\d{4}\b'

result = re.finditer(pattern, text)

result = [p.group(0) for p in result]

print (', '.join(result))


