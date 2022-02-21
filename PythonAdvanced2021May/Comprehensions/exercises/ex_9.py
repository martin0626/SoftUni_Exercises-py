bunker = {type_i: {'items': [], "quantity": 0, "quality": 0} for type_i in input().split(', ')}

n = int(input())
items_count = 0
quality_avg = 0

for _ in range(n):
    type_f, food, stats = input().split(' - ')
    first_s, second_s = stats.split(';')
    quantity = int(first_s.split(':')[1])
    quality = int(second_s.split(':')[1])
    items_count += quantity
    bunker[type_f]['items'].append(food)
    bunker[type_f]['quantity'] += quantity
    bunker[type_f]['quality'] += quality
    quality_avg += quality


print(f'Count of items: {items_count}')
print(f'Average quality: {(quality_avg / len(bunker)):.2f}')
[print(f'{k} -> {", ".join(v["items"])}') for k, v in bunker.items()]
