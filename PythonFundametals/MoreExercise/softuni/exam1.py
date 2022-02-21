days = int(input())
cookers = int(input())
cakes = int(input())
waffles = int(input())
pancakess = int(input())
cakes_sum = 45 * cakes
waffles_sum = 5.8 * waffles
pancakess_sum = 3.2 * pancakess
sum_1 = (cakes_sum + waffles_sum + pancakess_sum) * cookers) * days
sum_1 -= sum_1 * 1/8

print (f'{sum_1:.2f}')
