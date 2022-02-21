heroes = {name: {'items_n': 0, 'price': 0, 'items': []} for name in input().split(', ')}

while True:

    command = input()
    if command == 'End':
        break
    name, item, price = command.split('-')
    if item not in heroes[name]['items']:
        heroes[name]['items_n'] += 1
        heroes[name]['price'] += int(price)
        heroes[name]['items'].append(item)

[print(f'{n} -> Items: {v["items_n"]}, Cost: {v["price"]}') for n, v in heroes.items()]
