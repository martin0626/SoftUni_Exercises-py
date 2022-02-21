from math import floor
year = input()
p = int(input())
h = int(input())

weekend_play = (48 - h) * 3/4

party_play = p * 2/3
sum_all = weekend_play + party_play + h

if year == 'leap':
    sum_all += sum_all * 0.15

print (floor(sum_all))


