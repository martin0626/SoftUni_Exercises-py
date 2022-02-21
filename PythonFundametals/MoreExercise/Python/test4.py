import math
name = input()
budget = float(input())
beer = int(input())
chips = int(input())

def end_sum  (b, c):
    beer_sum = b * 1.20
    one_chips = beer_sum * 0.45
    sum_chips = one_chips * c
    end_sum1 = math.ceil(sum_chips) + beer_sum

    return end_sum1

if end_sum (beer, chips) <= budget:
    print (f'{name} bought a snack and has {budget - end_sum(beer, chips):.2f}leva left!')
else:
    print (f'{name} needs {budget - end_sum(beer, chips)} more leva!')