nums = ([float(el) for el in input().split()])

unique = []
for el in nums:
    if el not in unique:
        unique.append(el)

for num in unique:
    print(f'{num} - {nums.count(num)} times')
