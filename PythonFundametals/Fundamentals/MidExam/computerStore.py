prices = input()
taxes = 0
total_without_taxes = 0

def receipt (price_no_taxes, taxes_amount, total_price):
    return f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_no_taxes:.2f}$\nTaxes: {taxes_amount:.2f}$\n-----------\nTotal price: {total_price:.2f}$"



while True:
    if prices == 'special' or prices == 'regular':
        break
    prices = float(prices)
    if prices < 0:
        print ('Invalid price!')
        
    else:
        taxes += 0.2 * prices
        total_without_taxes += prices
    prices = input()

total_price = total_without_taxes + taxes
if prices == 'special':
    total_price -= 0.1 * total_price
if not total_price == 0:
    print (receipt(total_without_taxes, taxes, total_price))
else:
    print ('Invalid order!')

