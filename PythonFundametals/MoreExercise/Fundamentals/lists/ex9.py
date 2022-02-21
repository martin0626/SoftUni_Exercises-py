items = input().split('|')
budget = float(input())
profit = 0
item_prices = []
profit_for_all = 0

for x in items:
    item_by_item = x.split('->')
    type_c = item_by_item[0]
    price = float(item_by_item[1])

    if type_c == 'Clothes' and price <= 50 and budget >= price:
        budget -= price
        profit += 0.4 * price + price
        profit_for_all += 0.4 * price 
        item_prices.append(0.4 * price + price)
    elif type_c == 'Shoes' and price <= 35 and budget >= price:
        budget -= price
        profit += 0.4 * price + price
        profit_for_all += 0.4 * price 
        item_prices.append(0.4 * price + price)
    elif type_c == 'Accessories' and price <= 20.5 and budget >= price:
        budget -= price
        profit += 0.4 * price + price
        profit_for_all += 0.4 * price 
        new = 0.4 * price + price
        item_prices.append(new)
for x in item_prices:
    print (f'{x:.2f}', end = ' ')
    
print()


print (f'Profit: {profit_for_all:.2f}')
profit += budget
if profit >= 150:
    print ('Hello, France!')

else: 
    print ('Time to go.')



    