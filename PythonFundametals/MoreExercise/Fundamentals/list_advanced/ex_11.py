inventory = input().split(', ')
item = inventory[0]
inventory.append(inventory.pop(inventory.index(item)))

print (inventory)