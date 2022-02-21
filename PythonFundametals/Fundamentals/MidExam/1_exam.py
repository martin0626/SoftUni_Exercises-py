orders_count = int(input())
total = 0
for order in range (1, orders_count + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    coffe_price = days * capsules_count * price_per_capsule
    total += coffe_price
    print (f'The price for the coffee is: ${coffe_price:.2f}')

print (f'Total: ${total:.2f}')