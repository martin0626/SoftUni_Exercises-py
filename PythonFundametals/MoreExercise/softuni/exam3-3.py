cruise = input()
cabin = input()
days = int(input())
price_for_day = 0
if cabin == 'standard cabin':
    if cruise == 'Mediterranean':
        price_for_day = 27.5

    elif cruise == 'Adriatic':
        price_for_day = 22.99

    elif cruise == 'Aegean':
        price_for_day = 23

    
elif cabin == 'cabin with balcony':
    if cruise == 'Mediterranean':
        price_for_day = 30.2
    
    elif cruise == 'Adriatic':
        price_for_day = 25

    elif cruise == 'Aegean':
        price_for_day = 26.6

elif cabin == 'apartment':
    if cruise == 'Mediterranean':
        price_for_day = 40.5
    
    elif cruise == 'Adriatic':
        price_for_day = 34.99

    elif cruise == 'Aegean':
        price_for_day = 39.8

price = 0
price = days * price_for_day * 4
if days > 7:
    price -= price * 0.25

print (f"Annie's holiday in the {cruise} sea costs {price:.2f} lv.")
    
