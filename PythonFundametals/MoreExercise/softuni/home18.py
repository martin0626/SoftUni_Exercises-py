n = int(input())
price = float(input())
price_toy = int(input()) 
toy_sum = 0
money_saved = 0
counter_even = 0

for x in range (1, n + 1):
    if x % 2 == 0:
        counter_even += 1
        money_saved += 10 * counter_even

    if x % 2 != 0:
        money_saved += price_toy
diff = 0
money_saved -= counter_even
if price > money_saved:
    diff = price - money_saved
    print (f'No! {diff:.2f}')

elif price <= money_saved:
    diff = money_saved - price 
    print (f'Yes! {diff:.2f}')






