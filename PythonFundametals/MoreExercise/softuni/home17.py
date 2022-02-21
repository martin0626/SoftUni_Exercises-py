import math
year = input()
p = int(input())
h = int(input())

saturday_games = (48 - h) * 3/4
sunday_games = h
holiday_games = p * 2/3
sum_games = saturday_games + sunday_games + holiday_games 

if year == 'leap':
    sum_games += sum_games * 0.15
sum_games = math.floor(sum_games)
print (sum_games)