import re
text = input()

pattern = r'\b_(?P<result>[A-Za-z]+)\b'

id_finds = re.finditer(pattern, text)
list_results = []
for x in id_finds:
    rest = x.groupdict()
    list_results.append(rest["result"]) 
print (','.join(list_results))