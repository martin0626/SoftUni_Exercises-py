inventory = input().split(', ')
command = input()

while not command == 'Craft!':
    action, item = command.split(' - ')

    if action == 'Collect' and item not in inventory:
        inventory.append(item)
    elif action == 'Drop' and item in inventory:
        inventory.remove(item)
    elif action == 'Renew' and item in inventory:
        inventory.append(inventory.pop(inventory.index(item)))
    elif action == 'Combine Items':
        item_old, item_new = item.split(':')
        if item_old in inventory:
            index = inventory.index(item_old)
            inventory.insert(index + 1, item_new)
    command = input()
print (', '.join(inventory))
