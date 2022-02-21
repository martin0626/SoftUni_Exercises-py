cost = float(input())
mounths = int(input())
saved_monye = 0
for mounth in range (1, mounths + 1):
    
    if mounth % 2 != 0 and mounth != 1:
        saved_monye -= 0.16 * saved_monye
    if mounth % 4 == 0:
        saved_monye += 0.25 * saved_monye
    saved_monye += 0.25 * cost
    
if saved_monye >= cost:
    print (f'Bravo! You can go to Disneyland and you will have {(saved_monye - cost):.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {(cost - saved_monye):.2f}lv. more.')