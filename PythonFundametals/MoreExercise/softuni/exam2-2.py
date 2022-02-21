budget = int(input())
price_towel = float(input())
sale = int(input())

umbrella = price_towel * 2/3
flops = umbrella * 0.75
bag = (price_towel + flops) * 1/3
sum_all = umbrella + price_towel + flops + bag
sum_all -= sum_all * (sale/100)

if budget >= sum_all:
    print (f"Annie's sum is {sum_all:.2f} lv. She has {(budget - sum_all):.2f} lv. left.")
else:
    print (f"Annie's sum is {sum_all:.2f} lv. She needs {(sum_all - budget):.2f} lv. more.")