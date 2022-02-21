mouth = input()
hours_spend = float(input())
people = int(input())
time = input()

if mouth == 'March' or mouth == 'April' or mouth == 'May':
    if time == 'day':
        price = 10.5
    else:
        price = 8.4
else:
    if time == 'day':
        price = 12.6
    else:
        price = 10.2
price_for_man = price * hours_spend
if people >= 4:
    price_for_man -= price_for_man * 0.1
    price -= price * 0.1
    if hours_spend >= 5:
        price -= price * 0.5
        price_for_man -= price_for_man * 0.5
end_price = price_for_man * people 

print (f'Price per person for one hour: {price}')
print (f'Total cost of the visit: {end_price:.2f}')


    