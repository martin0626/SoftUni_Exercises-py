price = float(input())
puzzle = int(input())
barbies = int(input())
bear = int(input())
minions = int(input())
truck = int(input())

sum_all = puzzle * 2.6 + barbies * 3 + bear * 4.1 + minions * 8.2 + truck * 2
number_of_toys = puzzle + bear + minions + barbies + truck

if number_of_toys >= 50:
    sum_all -= sum_all * 0.25

sum_all -= sum_all * 0.1

if sum_all >= price:
    sum_all -= price
    print (f'Yes! {sum_all:.2f} lv left.')
else:
    price -= sum_all
    print (f'Not enough money! {price:.2f} lv needed.')