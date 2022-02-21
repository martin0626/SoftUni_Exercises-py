d = {'biggest': 10000, 'average': 2000, 'smallest':-234}
biggest = -100000
lower = 1000000
for x in d:
    if d[x] > biggest:
        biggest = d[x]
    if d[x] < lower:
        lower = d[x]

print (f'The biggest:{biggest}\nThe lower:{lower}')