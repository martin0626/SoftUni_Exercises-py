budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price_1l = flour_price * 1.25
milk_price_250ml = milk_price_1l / 4
current_cozonacs = 0
colored_eggs = 0
cozonac_price = milk_price_250ml + flour_price + eggs_price

while budget >= cozonac_price:
    budget -= cozonac_price
    current_cozonacs += 1
    if current_cozonacs % 3 == 0:
        colored_eggs -= current_cozonacs - 2
        colored_eggs += 3
    else:
        colored_eggs += 3

print (f'You made {current_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

