text = input().split(' ')
dict_1 = {}

for x in range (0, len(text), 2):
    key = text[x]
    value = text[x + 1]

    dict_1[key] = int(value)

print (dict_1)
