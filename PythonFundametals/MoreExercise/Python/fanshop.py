budget = int(input())
n = int(input())

for x in range (n):
    object = input()

    if object == 'hoodie':
        budget -= 30

    elif object == 'keychain':
        budget -= 4
    elif object == 'T-shirt':
        budget -= 20
    elif object == 'flag':
        budget -= 15
    else:
        budget -=1

if budget >= 0:
    print (f'You bought {n} item and left with {budget} lv.')
else:
    print (f'Not enough money you need {abs(budget)} more lv.')