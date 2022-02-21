budget = float(input())
season = input()
money_needed = 0
destination = ''
camp_or_hotel = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        money_needed = budget * 0.3

    elif season == 'winter':
        money_needed = budget * 0.7

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        money_needed = budget * 0.4

    elif season == 'winter':
        money_needed = budget * 0.8
else:
    destination = 'Europe'
    money_needed = budget * 0.9

if season == 'summer' and destination != 'Europe':
    camp_or_hotel = 'Camp'
else:
    camp_or_hotel = 'Hotel'

print (f'Somewhere in {destination}\n{camp_or_hotel} – {money_needed:.2f}')




    
