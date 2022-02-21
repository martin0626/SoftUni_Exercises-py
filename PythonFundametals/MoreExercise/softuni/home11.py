budget = int(input())
season = input()
fishers = int(input())
money_needed = 0
if season == 'Spring':
    money_needed = 3000
elif season == 'Summer' or season == 'Autumn':
    money_needed = 4200
elif season == 'Winter':
    money_needed = 2600

if fishers <= 6:
    money_needed -= money_needed * 0.1
elif 11 >= fishers > 6:
    money_needed -= money_needed * 0.15
elif fishers > 12:
    money_needed -= money_needed * 0.25

if season != 'Autumn' and fishers % 2 == 0:
    money_needed -= money_needed * 0.05



if budget >= money_needed:
    print (f'Yes! You have {(budget - money_needed):.2f} leva left.')
elif money_needed > budget:
    print (f'Not enough money! You need {(money_needed - budget):.2f} leva.')
    
    

    