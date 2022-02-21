elements = input().split()
bakery = {}

for x in range (0, len(elements), 2):
    key = elements[x]
    value = elements[x + 1]

    bakery[key] = int(value)

searched_products = input().split()

for product in searched_products:
    if product in bakery:
        print (f'We have {bakery[product]} of {product} left')

    else:
        print (f"Sorry, we don't have {product}")
