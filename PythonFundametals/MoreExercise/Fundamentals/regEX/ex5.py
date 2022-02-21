import re
all_commands = []
command = input()

while command != 'Purchase':
    all_commands.append(command)
    command = input()

pattern = r'>>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]+(\.[0-9]+)?)!(?P<quantity>[0-9]+)'
all_commands = ' '.join(all_commands)
results = re.finditer(pattern, all_commands)

total = 0
print (f'Bought furniture:')
for x in results:
    result = x.groupdict()
    print (result['furniture'])
    total += float(result['price']) * int(result['quantity'])
print (f'Total money spend: {total:.2f}')

{'furniture': Sofa, 'price'}