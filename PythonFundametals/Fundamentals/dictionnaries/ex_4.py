product_price = input()
products_price = {}
product_quantity = {}
while product_price != 'buy':
    key, quantity, value = product_price.split()
    value = float(value)
    quantity = float(quantity)
    if key not in products_price:
        products_price[key] = 0
    
    product_quantity[key] = quantity
    products_price[key] += value

    product_price = input()




for product, price  in products_price.items():
    for product_1, quantity in product_quantity.items():
        if product == product_1:
            price *= quantity
            break
    
    print (f'{product} -> {price:.2f}')
