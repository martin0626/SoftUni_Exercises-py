budget = float(input())
season = input()
money_needed = 0
destination = ''
camp_or_hotel = ''
if season == 'summer':
    if budget <= 100:
        money_needed = budget * 0.3
        destination = 'Bulgaria'
    elif 100 < budget <= 1000:
        destination = 'Balkans'
        money_needed = budget * 0.4
    elif budget > 1000:
        money_needed = budget * 0.9
        destination = 'Europe'




elif season == 'winter':
    if budget <= 100:
        money_needed = budget * 0.7
        destination = 'Bulgaria'
    elif 100 < budget <= 1000:
        money_needed = budget * 0.8
        destination = 'Balkans'
    elif budget > 1000:
        money_needed = budget * 0.9
        destination = 'Europe'

        
if season == 'summer' and destination != 'Europe':
    camp_or_hotel = 'Camp'
else:
    camp_or_hotel = 'Hotel'

print (f'Somewhere in {destination}\n{camp_or_hotel} – {money_needed:.2f}')


#NEW

