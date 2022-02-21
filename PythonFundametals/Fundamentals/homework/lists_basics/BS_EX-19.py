losts = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_count = 0
for x in range (1, losts + 1):
    if x % 2 == 0:
        expenses += helmet_price
    if x % 3 == 0:
        expenses += sword_price
        if x % 2 == 0:
            expenses += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                expenses += armor_price
print (f'Gladiator expenses: {expenses:.2f} aureus')
    