import math 
biscuit_for_day = int(input())
workers = int(input())
competition = int(input())
production = 0
for x in range (1, 31):
    if x % 3 == 0:
        production += math.floor(workers * (biscuit_for_day * 0.75))
    else:
        production += workers * biscuit_for_day
if production > competition:
    diff = ((production - competition)/competition) * 100
else:
    diff = ((competition - production)/competition) * 100
print (f'{production:.2f}')
print (f'{diff:.2f}')