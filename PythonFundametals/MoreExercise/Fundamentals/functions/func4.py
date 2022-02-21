product = input()
quantity = int(input())

def price (p, q):
    final_price = 0
    if p == 'coffee':
        final_price = q * 1.5
    elif p == 'water':
        final_price = q * 1
    elif p == 'coke':
        final_price = q * 1.4
    elif p == 'snacks':
        final_price = q * 2
    return final_price
print (f'{price (product, quantity):.2f}')
