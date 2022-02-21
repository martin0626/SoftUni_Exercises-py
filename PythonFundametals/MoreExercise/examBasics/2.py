price_twenty = float(input())
kg_bags = float(input())
days_left = int(input())
num_bags = int(input())

price_of_bag = 0

if kg_bags <= 10:
    price_of_bag = price_twenty * 0.2

elif 10 < kg_bags <= 20:
    price_of_bag = price_twenty * 0.5

elif kg_bags > 20:
    price_of_bag = price_twenty


total_price = price_of_bag * num_bags

if days_left > 30:
    total_price += total_price * 0.1
elif 7 <= days_left <= 30:
    total_price += total_price * 0.15
elif days_left < 7:
    total_price += total_price * 0.4

print (f'The total price of bags is: {total_price:.2f} lv.')