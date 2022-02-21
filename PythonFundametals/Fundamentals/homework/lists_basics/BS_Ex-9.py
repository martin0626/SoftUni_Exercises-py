quantity = int(input())
days = int(input())
price = 0
spirit = 0
for x in range (1, days + 1):
    if x % 11 == 0:
        quantity += 2
    
    if x % 2 == 0:
        price += 2 * quantity
        spirit += 5
    
    if x % 3 == 0:
        price += (5 * quantity + 3 * quantity)
        spirit += 13
    if x % 5 == 0:
        price += 15 * quantity
        spirit += 17
        if x % 3 == 0:
            spirit += 30


    if x % 10 == 0:
        spirit -= 20
        price += 23 
        if x == days:
            spirit -= 30


print (f'Total cost: {price}\nTotal spirit: {spirit}')