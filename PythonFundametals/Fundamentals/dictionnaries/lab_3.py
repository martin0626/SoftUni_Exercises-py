products = {}

command = input()


while command != 'statistics':
    product, num = command.split(': ')
    num = int(num)
    if product in products:
        products[product] += num 

    else:
        products[product] = num

    command = input()

print ('Products in stock:')
for (pr, qn) in products.items():
    print (f'- {pr}: {qn}')
print (f'Total Products: {len(products.keys())}')
print (f'Total Quantity: {sum(products.values())}')